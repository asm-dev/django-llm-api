# Integración de un LLM con Groq y Django

Este proyecto implementa un servicio capaz de generar respuestas a las preguntas del usuario mediante el uso de un modelo de lenguaje de gran tamaño o LLM. Actualmente, el modelo configurado es **llama3-8b-8192**, pero puede modificarse fácilmente desde `views.py` si se desea probar otros modelos disponibles en Groq.

&nbsp;

## Ejecución

1. (*Recomendable*) Generar un ecosistema de ejecución con Conda, `conda create -n nombre_del_entorno python=3.9` y `conda activate nombre_del_entorno` 
2. Registrarse en [Groq](https://console.groq.com) para obtener una API key
3. Crear un fichero `.env` en el directorio raíz que contenga `GROQ_API_KEY="la_api_key_conseguida"`
4. Clonar el repositorio en nuestra máquina e instalar las dependencias con `pip install django python-dotenv groq`
6. Desde la API en `/llm_api`, lanzar `python manage.py runserver` para ejecutar el servidor Django 
7. (*Opcional*) Probar el endpoint en `http://127.0.0.1:8000/groq/api/groq/`

&nbsp;

## Pruebas de uso

*Realizamos una request POST al endpoint usando RapidAPI*:

![image](https://github.com/user-attachments/assets/41403e1b-8a8f-483f-9405-62de20c24fdd)

*Comprobamos además que la información se almacena correctamente en la base de datos*:

![image](https://github.com/user-attachments/assets/3f87ffa0-1d15-4e76-b120-47f5c11b686b)

