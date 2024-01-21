import configuration
import requests
import data

# Запрос на создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_NEW_ORDER,
                         json=data.order_body)

# Запрос на получение заказа по номеру
def get_order_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + "?t=" + str(track_id))
# Александр Городечный, 12-я когорта — Финальный проект. Инженер по тестированию плюс