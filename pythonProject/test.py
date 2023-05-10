import pymongo
connection = pymongo.MongoClient("localhost",27017)
database = connection["my_db1"]
collection=database["my_col2"]
data=[
{"_id":1,'WinHtut':'CrazyCoder','age':26,'Hobby':'BuildingTools'},
{"_id":2,'Win':'CrazyCoder','age':26,'Hobby':'BuildingTools'},
{"_id":3,'Htut':'CrazyCoder','age':26,'Hobby':'BuildingTools'},
{"_id":4,'WinHtut1':'CrazyCoder','age':26,'Hobby':'BuildingTools'},
{"_id":5,'WinHtut2':'CrazyCoder','age':26,'Hobby':'BuildingTools'}
]
data={'_id':4,'name':'mgmg','age':23,'hobby':'reading'}
collection.insert_one(data)







