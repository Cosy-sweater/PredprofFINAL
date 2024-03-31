from pprint import pprint
import requests


def days_info():
    info_request = f"https://olimp.miet.ru/ppo_it_final/date"
    response = requests.get(info_request, headers={'X-Auth-Token': 'ppo_10_11932'})
    if not response:
        raise RuntimeError("Ошибка отправки запроса (404)")
    json_response = response.json()["message"]
    if not json_response:
        raise RuntimeError("Пустой json")
    pprint(json_response)
    return json_response


def room_info(day='25', month='01', year='23'):
    info_request = f"https://olimp.miet.ru/ppo_it_final?day={day}&month={month}&year={year}"
    response = requests.get(info_request, headers={'X-Auth-Token': 'ppo_10_11932'})

    if not response:
        raise RuntimeError("Ошибка отправки запроса (404)")
    json_response = response.json()["message"]
    if not json_response:
        raise RuntimeError("Пустой json")
    pprint(json_response)
    return json_response

days_info()
room_info()
