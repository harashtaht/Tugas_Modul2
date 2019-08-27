# ==================== No 3 : CSV & Json to MySQL ===========================

import mysql.connector, json, csv

# Connect to MySQL database
dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '####',
    database = 'converting2'
)

kursor = dbku.cursor()

#++++++++ CSV to MYSQL+++++++#

#++ Read data from CSV 
# Data dari CSV berbentuk String (semua)
# dataCSV = []
# with open('data_converting.csv', 'r', newline= '') as y:
#     readCSV = csv.DictReader(y)
#     for item in readCSV:
#         dataCSV.append(dict(item))
    # print(dataCSV)
# [{'ID': '3', 'Nama': 'Doraemon', 'Usia': '10'}, {'ID': '4', 'Nama': 'Shizuka', 'Usia': '12'},

#++ Create Table in Database MySQL
# query1 = '''CREATE TABLE datacsv (
#     ID int,
#     Nama text,
#     Usia int,
#     primary key (ID))'''
# kursor.execute(query1)

# Fetch Information on the Table
# kursor.execute('DESCRIBE datacsv')
# infoTable = kursor.fetchall()

# #++ Obtain name of Column in Table inside Database
# namaKolom = []
# for item in infoTable:
#     namaKolom.append(item[0])
# print(namaKolom)

# #++ Preparing data to insert to mySQL
# AllValues = []
# for item in dataCSV:
#     valueID = int(item[namaKolom[0]])
#     valueNama= (item[namaKolom[1]])
#     valueUsia = int(item[namaKolom[2]])
#     tupleValue = valueID, valueNama, valueUsia
#     AllValues.append(tupleValue)
# print(AllValues)

#++ Insert into mySQL
# query2 = '''INSERT into datacsv (ID, Nama, Usia) values
# (%s, %s, %s)'''
# kursor.executemany(query2, AllValues)
# dbku.commit()
# print(kursor.rowcount, 'data telah tersimpan')

#+++++ JSON to MYSQL +++++++#

# Create Table in Database MySQL (JSON)
# query1 = '''CREATE TABLE data_json (
#     nama varchar(50),
#     usia int,
#     kota varchar(50),
#     primary key(nama))'''

# #++ Creating Table Inside New Database
# kursor.execute(query1)

# #++ Information on the Table
# kursor.execute('DESCRIBE data_json')
# dataTable = kursor.fetchall()
# print(dataTable)

# #++ Obtain name of Column in Table inside Database
# namaKolom = []
# for item in dataTable:
#     namaKolom.append(item[0])
# print(namaKolom)

# #++ Read Data from Json
# with open ('data_converting.json') as x:
#     dataJason = json.load(x)
# print(dataJason[0])

# #++ Prepare data from Json, convert into Tuples (MySQL format)
# AllValuesJason = []
# for item in dataJason:
#     valueNama = item[namaKolom[0]]
#     valueUsia = int(item[namaKolom[1]])
#     valueKota = item[namaKolom[2]]
#     tupleValue = valueNama, valueUsia, valueKota
#     AllValuesJason.append(tupleValue)
# print(AllValuesJason)

#++ Inserting data from jason
# query2 = '''INSERT into data_json (nama, usia, kota) values
# (%s, %s, %s)'''
# kursor.executemany(query2, AllValuesJason)
# dbku.commit()
# print(kursor.rowcount, 'data telah tersimpan')