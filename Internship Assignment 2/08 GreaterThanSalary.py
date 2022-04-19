from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]


salary=int(input('Enter Salary : '))
dic={}
dic["salary"]=salary


jk={"$gt":dic}
#doc=coll.find(jk)
for doc in coll.find(dic,jk):
    print(doc)
