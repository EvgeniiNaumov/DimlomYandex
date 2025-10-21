import data
import sender_stand_request

def test_create_and_get_order():
    # Создаём заказ
    create_response = sender_stand_request.post_new_order(data.order_body)
    assert create_response.status_code == 201, f"Ошибка при создании заказа: {create_response.text}"
    track = create_response.json().get("track")
    assert track is not None, "В ответе отсутствует трек-номер"

    # Получаем заказ по треку
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200, f"Ошибка при получении заказа: {get_response.text}"
