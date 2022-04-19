from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=int(input('Enter worker ID : '))
qr={}
qr["_id"]=id

for doc in coll.find(qr):
    print (doc)

coll=db["exworkers"]
coll.insert_one(qr)
print ('Document Inserted into Exworkers Collection....')

coll=db["workers"]
coll.delete_one(qr)
print('Document Deleted From Workers Collection...')
