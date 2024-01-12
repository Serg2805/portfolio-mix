# sender_stand_request.py
import requests
import configuration
import data

# Функция создания юзера для полчения токена авторизации
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
            json=body,headers=data.headers)

# Функция для отправки POST-запроса на создание нового набора
def post_new_client_kit(auth_token, kit_body):
    url = configuration.URL_SERVICE + configuration.CREATE_KIT
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(url, json=kit_body, headers=headers)
    return response