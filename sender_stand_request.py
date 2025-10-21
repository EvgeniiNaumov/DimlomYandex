import requests
import configuration

def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.PATH_CREATE_ORDER, json=order_body)

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.PATH_GET_ORDER, params={"t": track})