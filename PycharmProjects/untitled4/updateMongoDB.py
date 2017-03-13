import time
from pymongo import MongoClient
# client = MongoClient("mongodb://Bobbys-MacBook-Pro.local:27000")
# db = client.admin
# coll = db.locations
# coll.find_one_and_update({'id': 'car1'}, {'$set': {'x': '200'}})



client = MongoClient("mongodb://192.168.128.210:27017/db")
db = client.admin
coll = db.locations
x = True
# coll.drop()
while x:
    coll.find_one_and_update({'id': 'car4'}, {'$inc': {'x': .5}})
    time.sleep(1)
