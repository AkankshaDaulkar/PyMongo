from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=int(input('Enter worker ID : '))
pq={}
pq["_id"]=id
print(pq)

for doc in coll.find(pq):
    print(doc)
