import requests
import pytest

URL_SERVICE = "https://4efbe2ad-4771-4a70-bc5e-604f1b3523ad.serverhub.praktikum-services.ru"

@pytest.fixture
def new_courier():
    """Данные курьера для теста"""
    return {
        "login": "ninja1",
        "password": "1234",
        "firstName": "Тест"
    }

def test_create_courier(new_courier):
    """
    Тест на создание курьера с фиксированными данными.
    Проверяет, что курьер создаётся и возвращается ok: true.
    """
    response = requests.post(f"{URL_SERVICE}/api/v1/courier", json=new_courier)
    
    assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"
    
    result = response.json()
    assert result.get("ok") is True, f"Courier not created: {result}"
    
    print(f"Курьер {new_courier['login']} успешно создан!")
