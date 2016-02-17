import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students
grades = db.grades

cursor = grades.find({"type": "homework"}).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)])

id = ''
for doc in cursor:
    if doc['student_id'] != id:
        id = doc['student_id']
        grades.remove({ '_id': doc['_id']})
