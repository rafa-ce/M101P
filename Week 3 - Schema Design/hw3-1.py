import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.school

students = db.students
cursor = students.aggregate([ { '$unwind' : '$scores' },
    { '$match' : { 'scores.type' : 'homework' } },
    { '$sort' : { '_id' : pymongo.ASCENDING, 'scores.score': pymongo.ASCENDING } }
])

id = ''
for doc in cursor:
    if doc['_id'] != id:
        id = doc['_id']
        students.update({ '_id': doc['_id']}, { '$pull': { 'scores': { 'score': doc['scores']['score'] } } } )
