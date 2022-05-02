import requests
import endpoints
from dataclasses import dataclass

bl = [
    "DOTA_Tooltip",
    "Рошан",
    "Карманный Рошан",
    "Aghanim\'s Shard — Рошан",
    "Aghanim\'s Blessing — Рошан",
    "Aghanim\'s Blessing",
    "Refresher Shard",
    "Cheese",
    "Aegis",
    "Overflowing Elixir",
    "Iron Talon",
    "Fallen Sky",
    "Necronomicon",
    "Animal Courier",
    "Flying Courier",
    "Infused Raindrops",
    "Gem of True Sight",
]

consumables = [
    "Town Portal Scroll",
    "Clarity",
    "Faerie Fire",
    "Smoke of Deceit",
    "Sentry Ward",
    "Варды",
    "Enchanted Mango",
    "Healing Salve",
    "Tango (не свой)",
    "Tango",
    "Tome of Knowledge",
    "Dust of Appearance",
    "Aghanim\'s Shard",
    "Bottle"
]


@dataclass
class Item:
    name: str
    localized_name: str
    cost: int
    secret_shop: bool
    recipe: bool
    parent_name: [str]


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
            return self._get_items_list_v2(response.json())
        else:
            print('Ошибка запроса')

    @staticmethod
    def _get_items_list(item_list):
        items = []

        if not item_list:
            return 'Ошибка! Список предметов не получен'
        for element in item_list.get('result').get("items"):
            items.append(Item(element['name'], element['localized_name'], element['cost'], element['secret_shop'],
                              element['recipe'], []))

        return items

    @staticmethod
    def _get_items_list_v2(item_list):
        items = []

        if not item_list:
            return 'Ошибка! Список предметов не получен'
        for element in item_list.get('result').get("items"):
            if element["localized_name"] in bl:
                pass
            elif element["localized_name"] in consumables:
                pass
            elif element["cost"] == 0:
                pass
            elif element["cost"] == 1:
                pass
            else:
                items.append(Item(element['name'], element['localized_name'], element['cost'], element['secret_shop'],
                                  element['recipe'], []))

        """Проверка на рецепты без айтема(было 2 штуки)"""
        for i in items:
            if i.localized_name.startswith("Рецепт:"):
                item = i.localized_name.replace("Рецепт: ", "")
                find = False
                for it in items:
                    if it.localized_name == item:
                        find = True
                if find:
                    pass
                else:
                    items.remove(i)

        return items

    def _preload_clear_items(self):
        response = requests.get(
            endpoints.GET_GAME_ITEMS, params={'key': self.token, 'language': 'ru'})
        if response.status_code == 200:
            return self._get_clear_items_list(response.json())
        else:
            print('Ошибка запроса')

    @staticmethod
    def _get_clear_items_list(item_list):
        items = []

        if not item_list:
            return 'Ошибка! Список героев не получен'
        for element in item_list.get('result').get("items"):
            if element['recipe'] == 1:
                pass
            elif element["cost"] == 0:
                pass
            elif element["localized_name"] in bl:
                pass
            elif element["localized_name"] in consumables:
                pass
            else:
                items.append(Item(element['name'], element['localized_name'], element['cost'], element['secret_shop'],
                                  element['recipe'], []))
        return items
