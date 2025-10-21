import requests
import pytest

URL_SERVICE = "https://4efbe2ad-4771-4a70-bc5e-604f1b3523ad.serverhub.praktikum-services.ru/api/v1"

@pytest.fixture
def new_order():
    return {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Пушкина, 1",
        "metroStation": 1,
        "phone": "+79991112233",
        "rentTime": 2,
        "deliveryDate": "2025-10-21",
        "comment": "Тестовый заказ",
        "color": ["BLACK"]
    }

def test_create_order_and_check(new_order):
    # Создание заказа
    create_response = requests.post(f"{URL_SERVICE}/orders", json=new_order)
    assert create_response.status_code in [200, 201]
    
    # Получаем трек заказа
    track_number = create_response.json().get("track")  # или "trackNumber" в зависимости от ответа
    assert track_number is not None

    # Получение заказа по треку (правильный query-параметр)
    get_response = requests.get(f"{URL_SERVICE}/orders/track", params={"t": track_number})
    assert get_response.status_code == 200

    order_data = get_response.json()
    print(f"Order {track_number} data: {order_data}")
