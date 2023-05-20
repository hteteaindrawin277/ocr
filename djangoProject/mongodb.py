import pymongo
connection = pymongo.MongoClient("localhost", 27017)
database = connection['my_db1']
collection = database['businessinfo2']
# query={'age':{'$gt':20}}
# query={'name':{'$regex':'^h'}}
# query={'age':20}

#myquery = {'year':2011}
#newdoc = {'$set': {'year':2023}}
try:
    for i in collection.find().limit(10):
        print(i)

    #collection.update_many(myquery, newdoc)
   # print('success')
    # collection.drop()
    # for i in range(100):
    # data = {'_id':i,'name': 'htet', 'age': 20, 'address': 'pol'}
    # d=collection.insert_one(data)
    # print('insert successfully',d.inserted_id)
    # for i in collection.find({},{'_id':0,'age':0}):
    # i=collection.delete_many(query)
    # print('deleted successfully',i.deleted_count)

except Exception as error:
    print(error)
