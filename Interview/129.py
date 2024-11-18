import csv
import json
import xmltodict


def read_csv_as_dictionary(filelocation):
    data_dict = {}
    with open(filelocation, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for row in csv_reader:
            data_dict[row['MDM Person Id']] = row
    return data_dict


filelocation = "C:\Build\Voya And SampleData\Person_10.csv"

data_dict = read_csv_as_dictionary(filelocation)

data_json = json.dumps(data_dict, indent=4)

print(data_json)
# print(json.dumps(data_dict["1"], indent=4, ensure_ascii=False))
