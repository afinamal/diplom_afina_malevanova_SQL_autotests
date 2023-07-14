import data
import configuration
import requests

def post_new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                             json=data.order_body)
    return response.json()["track"]

def get_new_track():
    return str(post_new_order())
def get_order_track():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH_TRACK
                            + "?t=" + get_new_track())
    return response

print(get_order_track())
