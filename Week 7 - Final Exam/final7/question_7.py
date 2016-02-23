import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.photo_sharing

images = db.images

cursor = images.find()

for doc in cursor:
    image_id = doc["_id"]
    i = db.albums.count( { "images" : image_id })

    if i < 1:
        images.delete_many( { "_id" : image_id})

print "Answer: ", images.count( { "tags" : "kittens"} )
