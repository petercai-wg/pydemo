from jproperties import Properties
from django.conf import settings
from django.db import connection
import os

from .domainobj import DropDownKeyValue


def getDBChoice(sql: str, filename: str) -> list:

    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    my_dict = getPropertiesDict(filename)

    choice_list = [(r[0],  my_dict.get(r[0])) for r in rows]

    return choice_list


def getPropertiesDict(filename: str) -> dict:
    filepath = os.path.abspath(os.path.join(
        str(settings.BASE_DIR) + '/Resources', filename + '.properties'))

    configs = Properties()
    with open(filepath, 'rb') as config_file:
        configs.load(config_file)
    items_view = configs.items()

    my_dict = {}
    for item in items_view:
        my_dict[item[0]] = item[1].data

    return my_dict


def getPropertiesList(filename: str) -> list:
    filepath = os.path.abspath(os.path.join(
        str(settings.BASE_DIR) + '/Resources', filename + '.properties'))

    configs = Properties()
    with open(filepath, 'rb') as config_file:
        configs.load(config_file)
    items_view = configs.items()

    configs_list = [DropDownKeyValue(item[0], item[1].data)
                    for item in items_view]

    return configs_list


def getPropertiesChoice(filename):
    filepath = os.path.abspath(os.path.join(
        str(settings.BASE_DIR) + '/Resources', filename + '.properties'))

    configs = Properties()
    with open(filepath, 'rb') as config_file:
        configs.load(config_file)
    items_view = configs.items()

    choice_list = [(item[0], item[1].data) for item in items_view]

    return choice_list


def getPropertiesJSONData(filename):
    configs = Properties()
    with open(filename + '.properties', 'rb') as config_file:
        configs.load(config_file)
    items_view = configs.items()

    data = [{'key': item[0], 'value': item[1].data} for item in items_view]

    return data
