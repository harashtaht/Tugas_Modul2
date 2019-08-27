# ==================== No 5 : MongoDB <-> Json =======================
import pymongo
import json

#++ Connect to MongoDb
x = pymongo.MongoClient('mongodb://localhost:27017')

#++ Create Database & Collection
#++ Mongo doesn't show collections if inside is empty
# Name of database 'converting', name of collection 'fromJason'

db_name = 'converting2'
coll_name = 'datafromCSV'
db_used = x[db_name]
coll_used = db_used[coll_name]

#++ Choosing Existing Database & Collections
# dbJas = x['converting']
# collectionJas = dbJas['fromJason']

#++ Check database inside MongoDB
# print('Current database inside Mongo:', x.list_database_names())

#++++ Converting Json to MongoDB ++++#
#++ Read Json File

with open ('data_converting.json') as x:
    dataJason = json.load(x)
# print(dataJason[0])
# ## [{'nama': 'Andi', 'usia': 19, 'kota': 'Jakarta'}, {'nama': 'Boyo', 'usia': 25, 'kota': 'Cimahi'},...]

# #++ Obtain name of Columns inside Json
namaKolom = []
for item in dataJason[0]:
    namaKolom.append(item)
# print(namaKolom)
# #namaKolom = ['nama', 'usia', 'kota']

# #++ Convert data Json into Mongo Format

# for item in dataJason:
#     inserting_data = coll_used.insert_one(item)
#     print(item[namaKolom[0]], item[namaKolom[1]], item[namaKolom[2]], 'inserted')
# print(list(coll_used.find()))

#++++ Converting MongoDB to Json ++++#

#+ Get Data from Collection in MongoDB
data_Mongo = list(coll_used.find())
#{'_id': ObjectId('5d5924d3960c65546f5679ea'), 'nama': 'Andi', 'usia': 19, 'kota': 'Jakarta'}

#+ Get Key from Collection
keyMongo = []
for item in data_Mongo:
    for key in item.keys():
        keyMongo.append(key)
keyMongo_ = list(sorted(set(keyMongo)))
# print(keyMongo_)

dataBersih = []
for item in data_Mongo:
    temp = {}
    for key, val in item.items():
        if key == '_id':
            temp[key] = str(val)
        else:
            temp[key] = val
    dataBersih.append(temp)
# print(dataBersih)

#++Write to Json++##
# with open ('no5_b.json', 'w') as x:
#     json.dump(dataBersih, x)
