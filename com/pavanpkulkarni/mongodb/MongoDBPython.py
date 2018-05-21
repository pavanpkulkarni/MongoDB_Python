import pymongo
from pymongo import MongoClient
import pprint


def ConnectToMongo (connectionString):
    try:
        print('Connecting to Mongo Client -', connectionString, '....')
        client = MongoClient(connectionString)
        db = client.super_hero_db
        collection = db.students
        print('Connection to Mongo Client ====== ', connectionString, ' ======= Successful...')
        print('Collection Details : ', collection)
    except Exception as e:
        print ('Unable to establish Connection : ', e)
    return collection


students = ConnectToMongo('mongodb://127.0.0.1:27017')



# Get one document
pprint.pprint(students.find_one())

#Count documents
print("Number of documents  : ", students.count())
print("Count with condition : ", students.find({'id':5}).count())

# Get all docs from MongoDB
for student in students.find():
    pprint.pprint(student)

for student in students.find({'id':2}):
    pprint.pprint(student)

# Insert document
newStudent = {
    "id": 13,
    "name":"Thanos",
    "courses_registered": [
        {   "CID": "CS003",
            "sem": "Spring_2011"},
        {	"CID": "CS002",
             "sem": "Summer_2011"},
        {	"CID": "CS001",
             "sem": "Fall_2011"}],
    "year_graduated": "2011"
    }

students.insert_one(newStudent)
print("After inserting new document")
for student in students.find({'id':13}):
    pprint.pprint(student)

# Delete document
students.delete_one({'id': 13})
print("After deleting new document")
for student in students.find({'id':13}):
    pprint.pprint(student)