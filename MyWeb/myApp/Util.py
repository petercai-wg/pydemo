from jproperties import Properties

from .forms import DropDownKeyValue


def getPropertiesList(filename):
    configs = Properties()
    with open(filename + '.properties', 'rb') as config_file:
        configs.load(config_file)
    items_view = configs.items()

    configs_list = [DropDownKeyValue(item[0], item[1].data)
                    for item in items_view]

    return configs_list


def getPropertiesJSONData(filename):
    configs = Properties()
    with open(filename + '.properties', 'rb') as config_file:
        configs.load(config_file)
    items_view = configs.items()

    data = [{'key': item[0], 'value': item[1].data} for item in items_view]

    return data
