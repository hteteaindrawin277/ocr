import pymongo
connection=pymongo.MongoClient('localhost',27017)
database=connection['my_db1']
collection=database['my_col1']
query={'_id':{'$gte':3}
try:

    data = collection.count({)
    print(data)

except Exception as error:
    print(error)