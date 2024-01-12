# create_kit_name_kit_test.py
import pytest
from sender_stand_request import post_new_user, post_new_client_kit
from data import kit_name_511_symbols, kit_name_512_symbols, user_body, one_symbol_name, empty_name, \
    english_letters, russian_letters, special_symbols, backspace_name, name_numbers, another_type_name

def get_kit_body(name):
    return {"name": name}

# Функция для получения токена авторизации
@pytest.fixture
def get_new_user_token():
    response = post_new_user(user_body)
    assert response.status_code == 201  # Ожидаем успешное создание пользователя
    auth_token = response.json().get("authToken")
    assert auth_token is not None  # Убеждаемся, что токен не пустой
    return auth_token


# Функция для позитивной проверки
def positive_assert(response, kit_body):
    assert response.status_code == 201
    assert response.json().get("name") == kit_body["name"]

# Функция для негативной проверки с кодом 400
def negative_assert_code_400(response):
    assert response.status_code == 400

def test_create_kit_one_symbol_name(get_new_user_token):
    kit_body = get_kit_body(one_symbol_name["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    positive_assert(response, kit_body)

def test_create_kit_too_long_name(get_new_user_token):
    kit_body = get_kit_body(kit_name_511_symbols["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    positive_assert(response, kit_body)

def test_create_kit_with_empty_name(get_new_user_token):
    kit_body = get_kit_body(empty_name["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    negative_assert_code_400(response)

def test_create_kit_over_possible_name(get_new_user_token):
    kit_body = get_kit_body(kit_name_512_symbols["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    negative_assert_code_400(response)

def test_create_kit_english_letters(get_new_user_token):
    kit_body = get_kit_body(english_letters["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    positive_assert(response, kit_body)

def test_create_kit_russian_letters(get_new_user_token):
    kit_body = get_kit_body(russian_letters["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    positive_assert(response, kit_body)

def test_create_kit_special_symbols(get_new_user_token):
    kit_body = get_kit_body(special_symbols["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    positive_assert(response, kit_body)

def test_create_kit_backspace_name(get_new_user_token):
    kit_body = get_kit_body(backspace_name["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    positive_assert(response, kit_body)

def test_create_kit_name_numbers(get_new_user_token):
    kit_body = get_kit_body(name_numbers["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    positive_assert(response, kit_body)

def test_create_kit_empty_parameter(get_new_user_token):
    kit_body = {}
    response = post_new_client_kit(get_new_user_token, kit_body)
    negative_assert_code_400(response)

def test_create_kit_another_type_name(get_new_user_token):
    kit_body = get_kit_body(another_type_name["name"])
    response = post_new_client_kit(get_new_user_token, kit_body)
    negative_assert_code_400(response)


if __name__ == "__main__":
    pytest.main()
