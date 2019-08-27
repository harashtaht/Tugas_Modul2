# ==================== No 2 : SQL -> CSV, Json =======================

import mysql.connector
import csv
import json

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '####',
    database = 'doraemon'
)
kursor = dbku.cursor()

# Obtain Column's name
query = '''DESCRIBE karakter'''
kursor.execute(query)
infoDB = kursor.fetchall()

namaKolom = []
for item in infoDB:
    namaKolom.append(item[0])
# print(namaKolom)

# Obtain data from table inside database
query1 = '''SELECT * FROM karakter'''
kursor.execute(query1)
dataDB = kursor.fetchall()

listFromSQL = []
for item in dataDB:
    dictDatabase = {}
    dictDatabase[namaKolom[0]] = item[0]
    dictDatabase[namaKolom[1]] = item[1]
    dictDatabase[namaKolom[2]] = item[2]
    listFromSQL.append(dictDatabase)
# print(listFromSQL)

##++ Part 1 : Write MySQL data to CSV

##-- Ngambil Data List consisted of Dictionaries dari atas ke CSV baru ('w')
# with open ('no2_a.csv', 'w', newline='') as y:
#     writeCSV = csv.DictWriter(y, namaKolom)
#     writeCSV.writeheader()
#     writeCSV.writerows(listFromSQL)

##++ Part 2 : Write SQL data to Json

# with open ('no2_b.json', 'w', newline='') as x:
#     json.dump(listFromSQL, x)