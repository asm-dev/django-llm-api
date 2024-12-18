import os
import json
from groq import Groq
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import QAEntry

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@method_decorator(csrf_exempt, name='dispatch')
class GroqAPIView(View):
    def post(self, request):
        try:
            body = json.loads(request.body)
            user_prompt = body.get("prompt")
            model = body.get("model")

            if not model:
                model = "llama3-8b-8192"

            if not user_prompt:
                return JsonResponse({"error": "Has de informar una prompt al modelo"})
            
            existing_entry = QAEntry.objects.filter(question=user_prompt).first()
            if existing_entry:
                return JsonResponse({"question": user_prompt, "response": existing_entry, "mode": "Se han reutilizado datos"}, status=200)
            
            chat_response = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_prompt}
                ],
                model=model,
                stream=False
            )

            response_content = chat_response.choices[0].message.content
            QAEntry.objects.create(question=user_prompt, answer=response_content)
            return JsonResponse({"question": user_prompt, "response": response_content}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es correcto"})
        except Exception as e:
            return JsonResponse({"error": "Se ha producido un error al procesar la pregunta"}, status=500)