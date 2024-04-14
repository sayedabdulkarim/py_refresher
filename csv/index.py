import csv

data = open("../example.csv", encoding="utf-8")

csv_data = csv.reader(data)

datalines = list(csv_data)

print(datalines)