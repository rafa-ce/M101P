import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.school

collection = db.students

for student in collection.find():
    scores = student["scores"]

    if scores[2]["type"] != "homework" or scores[3]["type"] != "homework":
        print ("ERRO")
        break

    if scores[2]["score"] < scores[3]["score"]:
        scores.pop(2)
    else:
        scores.pop(3)

    collection.update_one({'_id':student["_id"]}, {'$set': {'scores':scores}})

    print(scores)
