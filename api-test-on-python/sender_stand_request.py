# sender_stand_request.py
import requests
import configuration
import data

# Функция создания заказа
def post_create_order():
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    body = data.data_create_order
    response = requests.post(url,
            json=body, headers=data.headers)
    if response.status_code == 201:
        response_json = response.json()
        track_number = response_json["track"]
        return track_number
    else:
        return None

# Функция для получения заказа по его треку
def get_info_of_order(track_number):
    track_number_str = str(track_number)
    url = configuration.URL_SERVICE + configuration.GET_ORDER_INFO + track_number_str
    response = requests.get(url, headers=data.headers)
    return response
