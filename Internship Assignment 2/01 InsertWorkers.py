from pymongo import MongoClient

id=int(input('Enter employee ID : '))
nm=input('Enter name : ')
dp=input('Enter department : ')
ps=input('Enter post : ')
ct=input('Enter city : ')
sal=int(input('Enter salary : '))
mob=int(input('Enter mobile : '))
em=input('Enter email : ')

dic={}
dic["_id"]=id
dic["name"]=nm
dic["dept"]=dp
dic["post"]=ps
dic["city"]=ct
dic["salary"]=sal
dic["mobile"]=mob
dic["email"]=em

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

coll.insert_one(dic)
print('New worker added to MongoDB Collection')

