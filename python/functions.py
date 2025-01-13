# other_folder/python_functions.py
import g4f
from g4f.client import Client

def determine_model(prompt):
    # Используем g4f для отправки запроса
    query = "Что пользователь ожидает увидеть, если он отправляет запрос:\n" \
        + prompt + "\n1. Текст/код (любой ответ в текстовом виде)"\
        + "\n2.	Изображение/Рисунок/Картинку и так далее." \
        + "\nВыдай ответ в формате «1» или «2» без кавычек, который соответствует номеру одного из указанных вариантов."
    response = g4f.ChatCompletion.create(
        model="gpt-4o-mini",  # или "gpt-3.5-turbo", в зависимости от возможностей
        messages=[{"role": "user", "content": query}]
    )
    ans = ""
    for message in response:
        ans += message
    return ans 

def process_user_request_text_answer(prompt):
    # Используем g4f для отправки запроса
    response = g4f.ChatCompletion.create(
        model="gpt-4o-mini",  # или "gpt-3.5-turbo", в зависимости от возможностей
        messages=[{"role": "user", "content": prompt}]
    )
    ans = ""
    for message in response:
        ans += message
    return ans 

def process_user_request_image_answer(userPrompt):
    # Используем g4f для отправки запроса
    client = Client()
    response = client.images.generate(
        model="midjourney", 
        prompt=userPrompt,
        response_format="url"
    )
    image_url = response.data[0].url
    return image_url

