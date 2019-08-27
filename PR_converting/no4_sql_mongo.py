# ==================== No 4 : MongoDB <-> MySQL ======================= #

import mysql.connector
import pymongo

#++ Part 1
#++ Converting My SQL to Mongo ++#

#++Connect to MySQL database
# dbku = mysql.connector.connect(
#     host = '127.0.0.1',
#     port = 3306,
#     user = 'root',
#     passwd = '####',
#     database = 'converting'
# )

# kursor = dbku.cursor()
#++Connect to Mongo DB

# x = pymongo.MongoClient('mongodb://localhost:27017')


#-- Check Tables
# query1 = '''SHOW TABLES'''
# kursor.execute(query1)
# result = kursor.fetchall()
# print(result)

# #-- Information on the Table
# query2 = '''SELECT * FROM datacsv'''
# kursor.execute(query2)
# dataTable = kursor.fetchall()
# print(dataTable)
# Data berbentuk Tuples [('Andi', 19, 'Jakarta'), ('Boyo', 25, 'Cimahi'), ('Kampuang', 39, 'Sibolga'),

#== Obtain name of Column in Table inside Database
# query3 = '''DESCRIBE datacsv'''
# kursor.execute(query3)
# infoTable = kursor.fetchall()
# print(infoTable)

# namaKolom = []
# for item in infoTable:
#     namaKolom.append(item[0])
# print(namaKolom)

#++ Check Database inside Mongo
# print(x.list_database_names())

# db_name = 'converting'
# coll_name = 'fromSQL'
# db_used = x[db_name]
# coll_used = db_used[coll_name]

# list_dataSQL = []
# for data in dataTable:
#     dict_dataSQL = {}
#     dict_dataSQL[namaKolom[0]] = data[0]
#     dict_dataSQL[namaKolom[1]] = data[1]    
#     dict_dataSQL[namaKolom[2]] = data[2]
#     list_dataSQL.append(dict_dataSQL)
# # print(list_dataSQL)

#++ Insert data to MongoDB

# for item in list_dataSQL:
#     inserting_data = coll_used.insert_one(item)
#     print(item[namaKolom[0]], item[namaKolom[1]], item[namaKolom[2]], 'inserted')
# print(list(coll_used.find()))

#++ Part 2
#++ Converting Mongo to MySQL ++#

#++ Connecting to Mongo
db_connect = pymongo.MongoClient('mongodb://localhost:27017')
# print(db_connect.list_database_names())

# #++Choosing Database & Collection
# db_name = 'converting'
# coll_name = 'fromCSV'
# db_used = db_connect[db_name]
# coll_used = db_used[coll_name]

#++Get list from Collection in MongoDB
# data_Mongo = list(coll_used.find())
# print(data_Mongo[0])
# List consisting of Dict [{'_id': ObjectId('5d59380c464bc5902a7141b8'), 'ID': '3', 'Nama': 'Doraemon', 'Usia': '10'}

# namaKolom = []
# for item in data_Mongo[0]:
#     namaKolom.append(item)
# print(namaKolom)
# ['_id', 'ID', 'Nama', 'Usia']

#++ Create Database and Tables in MySQL

dbku = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '###',
    database = 'converting'
)

kursor = dbku.cursor()

# query1 = '''CREATE TABLE data_mongo (
#     _id varchar(50),
#     ID int,
#     Nama varchar(50),
#     Usia int,
#     primary key(ID)
# )'''
# kursor.execute(query1)

#-- Information on the Table in MySQL
# kursor.execute('DESCRIBE data_mongo')
# infoTable = kursor.fetchall()
# print(infoTable)

#-- Check what's in the table
# query2 = '''SELECT * from data_mongo'''
# kursor.execute(query2)
# dataTable = kursor.fetchall()
# print(dataTable)

#-- Write Data to SQL

#++ Prepare data from Mongo into SQL format
# AllValuesMongo = []
# for item in data_Mongo:
#     value_id = str(item[namaKolom[0]])
#     valueID = int(item[namaKolom[1]])
#     valueNama = item[namaKolom[2]]
#     valueUsia = int(item[namaKolom[3]])
#     tupleValue = value_id, valueID, valueNama, valueUsia
#     AllValuesMongo.append(tupleValue)
# print(AllValuesMongo)

#++ Inserting data into SQL
# query3 = '''INSERT into data_mongo (_id, ID, Nama, Usia) values (%s, %s, %s, %s)'''
# kursor.executemany(query3, AllValuesMongo)
# dbku.commit()
# print(kursor.rowcount, 'data telah tersimpan')