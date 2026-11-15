# Integrating an LLM with Groq and Django

This project implements a service capable of generating answers to user questions using a large language model (LLM). The model currently configured is **llama3-8b-8192**, but it can easily be changed in `views.py` if you want to try other models available on Groq.

&nbsp;

## Running the project

1. (*Recommended*) Create an execution environment with Conda, `conda create -n nombre_del_entorno python=3.9` and `conda activate nombre_del_entorno` 
2. Sign up at [Groq](https://console.groq.com) to get an API key
3. Create a `.env` file in the root directory containing `GROQ_API_KEY="la_api_key_conseguida"`
4. Clone the repository to our machine and install the dependencies with `pip install django python-dotenv groq`
6. From the API in `/llm_api`, run `python manage.py runserver` to start the Django server 
7. (*Optional*) Try the endpoint at `http://127.0.0.1:8000/groq/api/groq/`

&nbsp;

## Usage tests

*We send a POST request to the endpoint using RapidAPI*:

![image](https://github.com/user-attachments/assets/41403e1b-8a8f-483f-9405-62de20c24fdd)

*We check that the information is stored correctly in the database*:

![image](https://github.com/user-attachments/assets/3f87ffa0-1d15-4e76-b120-47f5c11b686b)

