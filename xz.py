import requests
import sys


def degree(obj):
    corners = obj['boundedBy']['Envelope']
    left_bottom, right_upper = corners['lowerCorner'].split(), corners['upperCorner'].split()
    return str(abs((float(left_bottom[0]) - float(right_upper[0])) / 2)), \
           str(abs((float(left_bottom[1]) - float(right_upper[1])) / 2))


def show_image(x_coor, y_coor):
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": " ",
        "format": "json"}
    response = requests.get("http://geocode-maps.yandex.ru/1.x/", params=geocoder_params)
    toponym = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_longitude, toponym_lattitude = x_coor, y_coor
    spn = degree(toponym)
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),  # корды
        "spn": ",".join(spn),
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude])}
    with open('out.jpg', 'wb') as out_file:
        out_file.write(requests.get("http://static-maps.yandex.ru/1.x/", params=map_params).content)