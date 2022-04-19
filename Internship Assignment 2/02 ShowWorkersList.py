from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

for doc in coll.find():
    #print(doc)
    try:
        print('%s | %s | %s | %s | %d | %d | %s' %(doc['name'],doc ['dept'],doc['post'],doc['city'],doc['salary'],doc['mobile'],doc['email']))
    except:
        pass
