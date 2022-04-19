from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

dp=input('Enter department : ')
pq={}
pq["dept"]=dp
print(pq)

for doc in coll.find(pq):
    print(doc)