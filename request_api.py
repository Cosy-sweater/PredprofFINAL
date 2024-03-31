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
    return json_response


def room_info(day='25', month='01', year='23'):
    info_request = f"https://olimp.miet.ru/ppo_it_final?day={day}&month={month}&year={year}"
    response = requests.get(info_request, headers={'X-Auth-Token': 'ppo_10_11932'})

    if not response:
        raise RuntimeError("Ошибка отправки запроса (404)")
    json_response = response.json()["message"]
    if not json_response:
        raise RuntimeError("Пустой json")
    return json_response


def func_lights_in_all_rooms(count_room=None, windows=None):
    res_lst = []
    for day in days_info():
        room = room_info(*day.split('-'))
        lst_personal_numbers_rooms = []
        lst_is_light = []
        if not (windows is None) and room['windows_for_flat']['data'] != windows:
            continue
        if not (count_room is None) and len(room['windows_for_flat']['data']) != count_room:
            continue
        for i in range(len(room['windows']['data'])):
            floor_lst = [] * sum(map(int, room['windows_for_flat']['data']))
            for k, j in enumerate(room['windows_for_flat']['data']):
                floor_lst.extend([i * 3 + k + 1] * j)
            lst_personal_numbers_rooms.append(floor_lst)
            lst_is_light.append(room['windows']['data'][f'floor_{i + 1}'])
        res_lst.append((lst_personal_numbers_rooms[::-1], lst_is_light[::-1]))
    return res_lst


pprint(func_lights_in_all_rooms())
