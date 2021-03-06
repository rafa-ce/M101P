#####Final: Question 7

You have been tasked to cleanup a photo-sharing database. The database consists of two collections, albums, and images. Every image is supposed to be in an album, but there are orphan images that appear in no album. Here are some example documents (not from the collections you will be downloading).

```
> db.albums.findOne()
{
	"_id" : 67
	"images" : [
		4745,
		7651,
		15247,
		17517,
		17853,
		20529,
		22640,
		27299,
		27997,
		32930,
		35591,
		48969,
		52901,
		57320,
		96342,
		99705
	]
}

> db.images.findOne()
{ "_id" : 99705, "height" : 480, "width" : 640, "tags" : [ "dogs", "kittens", "work" ] }
```

From the above, you can conclude that the image with *_id* = 99705 is in album 67. It is not an orphan.

Your task is to write a program to remove every image from the images collection that appears in no album. Or put another way, if an image does not appear in at least one album, it's an orphan and should be removed from the images collection.

Download final7.zip from [Download Handout](https://university.mongodb.com/static/MongoDB_2016_M101P_January/handouts/final7.55e3678c7664.zip) link and use mongoimport to import the collections in albums.json and images.json.

When you are done removing the orphan images from the collection, there should be 89,737 documents in the images collection. To prove you did it correctly, what are the total number of images with the tag 'kittens" after the removal of orphans? As as a sanity check, there are 49,932 images that are tagged 'kittens' before you remove the images.
Hint: you might consider creating an index or two or your program will take a long time to run.

:white_medium_square: 49,932

:white_medium_square: 47,678

:white_medium_square: 38,934

:white_medium_square: 45,911

:white_medium_square: 44,822

#####Answer: 44,822

Import the collections in albums.json and images.json

```
$ mongoimport -d photo_sharing -c albums < albums.json
2016-02-23T01:34:26.548+0000	connected to: localhost
2016-02-23T01:34:26.801+0000	imported 1000 documents
$ mongoimport -d photo_sharing -c images < images.json
2016-02-23T01:34:41.316+0000	connected to: localhost
2016-02-23T01:34:44.313+0000	photo-sharing.images	7.8 MB
2016-02-23T01:34:44.886+0000	photo-sharing.images	9.2 MB
2016-02-23T01:34:44.887+0000	imported 100000 documents
```

Create index for images in the album:
```
> db.albums.createIndex( { images : 1} )
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}
```

Create index for tags:
```
> db.images.createIndex( { tags : 1} )
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}
```

Run question_7.py
```
$ python question_7.py 
Answer:  44822
```
