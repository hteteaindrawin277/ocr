import pymongo
connection = pymongo.MongoClient("localhost", 27017)
database = connection['my_db1']
collection = database['my_col1']
#query={'_id':8,'name':'aye','age':24,'hobby':'reading'}
try:

    collection.rename('my_col1', 'my_new')

   # data=collection.remove({'age': { '$gt': 20}},1)
    #data=collection.find().pretty()
    #for i in collection.find().count('name'):
    #print(data)

   #data=collection.create_index()
     #  print(i)
except Exception as error:
    print(error)