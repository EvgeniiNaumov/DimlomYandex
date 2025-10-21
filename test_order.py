import sender_stand_request
import data

#Наумов Евгений,35 кагорта, диплотный проект
class TestCreateOrder:
    def test_create_order_and_get_by_track_success(self):
        # Создаем заказ
        create_response = sender_stand_request.create_order(data.OrderData.ORDER_BODY)
        
        # Проверяем успешное создание и получаем трек
        assert create_response.status_code == 201
        track = create_response.json()["track"]
        
        # Получаем заказ по треку
        get_response = sender_stand_request.get_order_by_track(track)
        
        # Основная проверка теста: заказ должен быть найден
        assert get_response.status_code == 200
        assert "order" in get_response.json()