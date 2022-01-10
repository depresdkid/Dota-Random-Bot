import requests

import endpoints


class Api(object):
    def __init__(self, token):
        self.token = token
        self.heroes = self._preload_heroes()
        self.items = self._preload_items()

    def _preload_heroes(self):
        response = requests.get(
            endpoints.GET_HEROES, params={'key': self.token, 'language': 'ru'})
        if response.status_code == 200:
            return self._get_hero_list(response)
        else:
            print('Ошибка запроса')

    def _get_hero_list(self, hero_list):
        hero_names = []
        hero_list = hero_list.json().get('result').get('heroes')
        if not hero_list:
            return 'Ошибка! Список героев не получен'
        for element in hero_list:
            hero_names.append(element['localized_name'])
        return hero_names

    def _preload_items(self):
        response = requests.get(
            endpoints.GET_GAME_ITEMS, params={'key': self.token, 'language': 'ru'})
        if response.status_code == 200:
            return self._get_items_list(response)
        else:
            print('Ошибка запроса')

    def _get_items_list(self, item_list):
        items_name = []
        item_list = item_list.json().get('result').get("items")
        if not item_list:
            return 'Ошибка! Список героев не получен'
        for element in item_list:
            items_name.append(element['localized_name'])
        return items_name
