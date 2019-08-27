# ==================== No 6 : MongoDB <-> CSV =======================
import pymongo
import csv

# Part A: MongoDB to CSV

#++ Connecting to Mongo
db_connect = pymongo.MongoClient('mongodb://localhost:27017')
print(db_connect.list_database_names())

# #++Choosing Database & Collection
# db_name = 'fantastic4'
# coll_name = 'daftarAnggota'
# db_used = db_connect[db_name]
# coll_used = db_used[coll_name]

#++Get list from Collection in MongoDB
# data_Mongo = list(coll_used.find())
# print(data_Mongo[0])
# [{'_id': ObjectId('5d58f4a3b2e27928f0ac4d15'), 'nama': 'Bambang', 'usia': 29.0}, {'_id': ObjectId('5d58f9652fa65010164dd085'), 'nama': 'Budiono', 'usia': '29'},


# namaKolom = []
# for item in data_Mongo[0]:
#     namaKolom.append(item)
# print(namaKolom)

##++ Write MongoDB data to CSV 
# with open ('no6_a.csv', 'w', newline='') as x:
#     writeCSV = csv.DictWriter(x, namaKolom)
#     writeCSV.writeheader()
#     writeCSV.writerows(data_Mongo)

##Part B: CSV to MongoDB

#++Choosing Database & Collection
db_name = 'converting2'
coll_name = 'fromCSV'
db_used = db_connect[db_name]
coll_used = db_used[coll_name]

# #++Read data CSV
dataCSV = []
with open('data_converting.csv', 'r', newline= '') as CsvToMon:
    readCSV = csv.DictReader(CsvToMon)
    for item in readCSV:
        dataCSV.append(dict(item))
# print(dataCSV)

namaKolom= []
for item in dataCSV[0]:
    namaKolom.append(item)

# for item in dataCSV:
#     inserting_data = coll_used.insert_one(item)
#     print(item[namaKolom[0]], item[namaKolom[1]], item[namaKolom[2]], 'inserted')
# print(list(coll_used.find()))
