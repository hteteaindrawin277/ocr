import pymongo
uri = 'mongodb+srv://root:toor@cluster0.hb6fzin.mongodb.net/?retryWrites=true&w=majority'
connection=pymongo.MongoClient(uri)
database =connection['my_db1']
collection=database['my_col1']
#query={'_id':{'$eq':3}}
query={'_id':{'$in':[2,5]}}
#query={'_id':{'$ne':3}}
#query={'_id':{'$nin':[3,6]}}
#query={'_id':{'$gte':3}}

try:
    for i in collection.find(query):
        print(i)

    #for i  in range(10):
        #data={'_id':i,'name':'mumu','age':16,'hobby':'writing'}
        #d=collection.insert_one(data)
        #print(d)

    #for i in collection.find(query):
      #  print(i)

except Exception as error:
    print(error)