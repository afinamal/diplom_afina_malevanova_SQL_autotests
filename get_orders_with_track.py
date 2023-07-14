# Афина Малеванова, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

def test_check_status_is_200():
    assert sender_stand_request.get_order_track().status_code == 200
