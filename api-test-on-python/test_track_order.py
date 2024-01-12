#test_track_order.py
import pytest
import sender_stand_request


@pytest.mark.test
def test_track_order():
    # function for create an order
    track_number = sender_stand_request.post_create_order()

    response_of_track_order = sender_stand_request.get_info_of_order(track_number)

    assert response_of_track_order.status_code == 200, "Тест успешно пройден"
