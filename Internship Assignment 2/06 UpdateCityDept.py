from pymongo import MongoClient

id= int(input('Enter Employee ID : '))
pq={}
pq["_id"]=id
client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

for doc in coll.find(pq):
    print(doc)

#print(pq)

ct=input('Enter new city : ')
ch={}
ch["city"]=ct
print(ch)
upd={"$set":ch}


dep=input('Enter new department:')
jk={}
jk["dept"]=dep
print(jk)

uad={"$set":jk}

coll.update_one(pq,upd)
coll.update_one(pq,uad)

print('document updated....')
