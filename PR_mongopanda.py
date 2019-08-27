import pandas as pd
# from pymongo import MongoClient
import pymongo

##### Connecting to MongoDB
db_connect = pymongo.MongoClient('mongodb://localhost:27017')
# print(db_connect.list_database_names())
# database_name = 'converting2'
database_used = db_connect['converting2']
collection_used = database_used['fromCSV']
data = list(collection_used.find())
# print(data)

##### Converting to Pandas

df = pd.DataFrame(data)
df.set_index('_id', inplace=True)
# print(df)