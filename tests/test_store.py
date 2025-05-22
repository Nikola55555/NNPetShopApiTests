import allure
import jsonschema
import pytest
import requests
from .schemas.store_schema import STORE_SCHEMA

BASE_URL = "http://5.181.109.28:9090/api/v3"


@allure.feature("Store")
class TestStore:
    @allure.title("Размещение заказа")
    def test_add_order(self):
        with allure.step("Подготовка данных для создания заказа"):
            payload = {
                "id": 1,
                "petId": 1,
                "quantity": 1,
                "status": "placed",
                "complete": True
            }

        with allure.step("Отправка запроса на размещение заказа"):
            response = requests.post(url=f"{BASE_URL}/store/order", json=payload)
            response_json = response.json()

        with allure.step("Проверка статуса ответа и валидация JSON-схемы"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            jsonschema.validate(response_json, STORE_SCHEMA)

        with allure.step("Проверка параметров заказа в ответе"):
            assert response_json['id'] == payload['id'], "id заказа не совпадает с ожидаемым"
            assert response_json['petId'] == payload['petId'], "id питомца не совпадает с ожидаемым"
            assert response_json['quantity'] == payload['quantity'], "количество не совпадает с ожидаемым"
            assert response_json['status'] == payload['status'], "статус не совпадает с ожидаемым"
            assert response_json['complete'] == payload['complete']

            # with allure.step("Проверка текстового содержимого ответа"):
        #     assert response.text == "Pet deleted", "Текст ответа не совпал с ожидаемым"
