import requests
import endpoints
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    localized_name: str
    cost: int
    recipe: bool


class Api(object):
    def __init__(self, token):
        self.token = token
        self.heroes = self._preload_heroes()
        self.items = self._preload_items()
        self.clear_items = self._preload_clear_items()

    def _preload_heroes(self):
        response = requests.get(
            endpoints.GET_HEROES, params={'key': self.token, 'language': 'ru'})
        if response.status_code == 200:
            return self._get_hero_list(response)
        else:
            print('Ошибка запроса')

    @staticmethod
    def _get_hero_list(hero_list):
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

    @staticmethod
    def _get_items_list(item_list):
        items_name = []

        if not item_list:
            return 'Ошибка! Список предметов не получен'
        for element in item_list.json().get('result').get("items"):
            items_name.append(Item(element['name'], element['localized_name'], element['cost'], element['recipe']))
        return items_name

    def _preload_clear_items(self):
        response = requests.get(
            endpoints.GET_GAME_ITEMS, params={'key': self.token, 'language': 'ru'})
        if response.status_code == 200:
            return self._get_clear_items_list(response)
        else:
            print('Ошибка запроса')

    @staticmethod
    def _get_clear_items_list(item_list):
        items_name = []

        if not item_list:
            return 'Ошибка! Список героев не получен'
        for element in item_list.json().get('result').get("items"):
            if element['recipe'] == 1 \
                    or element["cost"] == 0 \
                    or "DOTA_Tooltip" in element["localized_name"] \
                    or "Aegis" in element["localized_name"] \
                    or "Refresher Shard" in element["localized_name"] \
                    or "Cheese" in element["localized_name"] \
                    or "Рошан" in element["localized_name"]:
                pass
            else:
                items_name.append(Item(element['name'], element['localized_name'], element['cost'], element['recipe']))
        return items_name

