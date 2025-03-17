import csv

with open(
    "C:\Build\Voya And SampleData\Person_10.csv", mode="r", encoding="utf-8"
) as file:
    csv_reader = csv.reader(file, delimiter=";", skipinitialspace=True)
    header = next(csv_reader)
    print(type(csv_reader))
    print(type(header))
    print(header)
    for row in csv_reader:
        print(type(row))
        print(row)
        for element in row:
            print(str(type(element)) + ":" + element)
