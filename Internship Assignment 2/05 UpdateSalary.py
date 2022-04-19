from pymongo import MongoClient

id= int(input('Enter Employee ID : '))
pq={}
pq["_id"]=id

print(pq)

salary=int(input('Enter Salary : '))
ch={}
ch["salary"]=salary

print(ch)

upd={"$set":ch}

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

coll.update_one(pq,upd)
for doc in coll.find(pq):
    print(doc)
    

