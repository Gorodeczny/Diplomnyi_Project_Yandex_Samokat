import new_request

# Проверка на зоздание заказа
def test_order_creation():
   creation_response = new_request.post_new_order()
   track_id = creation_response.json()['track']
   response = new_request.get_order_track(track_id)
   assert response.status_code == 200
# Проверка, что код ответа = 200






