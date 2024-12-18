import os
import json
from groq import Groq
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@method_decorator(csrf_exempt, name='dispatch')
class GroqAPIView(View):
    def post(self, request):
        try:
            body = json.loads(request.body)
            user_prompt = body.get("prompt")

            if not user_prompt:
                return JsonResponse({"error": "Has de informar una prompt al modelo"})
            
            chat_response = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_prompt}
                ],
                model = "llama3-8b-8192",
                stream=False
            )

            response_content = chat_response.choices[0].message.content
            return JsonResponse({"question": user_prompt, "response": response_content}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es correcto"})
        except Exception as e:
            return JsonResponse({"error": "Se ha producido un error al procesar la pregunta"}, status=500)