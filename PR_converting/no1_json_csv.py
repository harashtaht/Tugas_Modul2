# ==================== No 1 : Json <-> CSV ===========================
import json
import csv

#Load data from Json
with open ('data_converting.json') as x:
    data_json = json.load(x)
# print(data_json)

##++++++ Write Json Data to CSV

# with open ('no1_a.csv', 'w', newline = '') as csvCreate:
#     readJson = csv.DictWriter(csvCreate, fieldnames= ['nama', 'usia', 'kota'])
#     readJson.writeheader()
#     readJson.writerows(data_json)

##+++++++ Write CSV data to Json

##-- Load CSV Data
dataCSV = []
with open ('data_converting.csv', 'r', newline= '') as y:
    readCSV = csv.DictReader(y)
    for item in readCSV:
        dataCSV.append(dict(item))
##[{'ID': '3', 'Nama': 'Doraemon', 'Usia': '10'}, {'ID': '4', 'Nama': 'Shizuka', 'Usia': '12'},

with open ('no1_b.json', 'w', newline='') as jsonCreate:
    json.dump(dataCSV, jsonCreate)