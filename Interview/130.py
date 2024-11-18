import csv
import json
import xmltodict
import xml
from pydantic import BaseModel, ValidationError


class Item(BaseModel):
    identifier: int
    category: str
    brand: str
    name: str
    available: bool
    defaultPrice: float


filelocation = "C:\Build\Voya And SampleData\Store\Items.xml"


with open(filelocation, "r", encoding="utf-8") as file:
    xml_data = file.read()
    item_list = []
    # print(xml_data)
    data_dict = xmltodict.parse(xml_data)
    # print(json.dumps(data_dict['root'], indent=4))
    # total_price = sum(int(item['defaultPrice'])
    #                   for item in data_dict['root']['Item'])

    # print(sum(int(item['defaultPrice']) for item in data_dict['root']['Item']))

    # print(json.dumps(data_dict, indent=4))
    items = list(data_dict['root']['Item'])
    for item in items:
        try:
            formatted_item = Item(**item)
            item_list.append(formatted_item)
        except ValidationError as e:
            print(f"Validation error for item {item}: {e}")


print(sum(float(item.defaultPrice) for item in item_list))
