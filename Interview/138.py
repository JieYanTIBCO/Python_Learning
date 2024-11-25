import pandas as pd
import sqlite3
import csv
import json

csv_file = r"C:\Users\Jackie\Employee_export.csv"
json_file = r"C:\Users\Jackie\Employee_export.json"

with open(csv_file, "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    data_list = [row for row in reader]
    for record in data_list:
        record.pop("HireDate", None)

    print(data_list)
    # for row in reader:
    #     print(row)

    # data_json = json.dumps(data_list, indent=4)

    with open(json_file, "w", encoding="utf-8") as json_file:
        json.dump(data_list, json_file, indent=4)


# df.to_csv(output_csv, index=False)

# # print(f"Employee 表已导出到 {output_csv}")
