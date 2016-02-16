###### Homework: Homework 1.1

Install MongoDB on your computer and run it on the standard port.

Download the HW1-1 from the [Download Handout](https://university.mongodb.com/static/MongoDB_2016_M101P_January/handouts/hw1-1.184820ec29b6.zip) link and uncompress it.

Use mongorestore to restore the dump into your running mongod. Do this by opening a terminal window (mac) or cmd window (windows) and navigating to the directory so that you are in the parent directory of the dump directory (if you used the default extraction method, it should be hw1/). Now type:

``
$ mongorestore dump
``

Note you will need to have your path setup correctly to find mongorestore.

Next, go into the Mongo shell, perform a findOne on the collection called hw1 in the database m101. That will return one document. Please provide the value corresponding to the "answer" key from the document returned.

*hint: if you get back a document that looks like { "_id": 1234, "answer": 2468 }, please only put in 2468 (with no spaces) for your answer.*

###### Answer: 42
```
$ mongorestore dump
2016-02-15T23:30:23.281+0000	building a list of dbs and collections to restore from dump dir
2016-02-15T23:30:23.293+0000	reading metadata for m101.hw1 from
2016-02-15T23:30:23.295+0000	reading metadata for m101.funnynumbers from
2016-02-15T23:30:23.296+0000	restoring m101.hw1 from
2016-02-15T23:30:23.302+0000	restoring m101.funnynumbers from
2016-02-15T23:30:23.320+0000	restoring indexes for collection m101.hw1 from metadata
2016-02-15T23:30:23.321+0000	finished restoring m101.hw1 (1 document)
2016-02-15T23:30:23.347+0000	restoring indexes for collection m101.funnynumbers from metadata
2016-02-15T23:30:23.348+0000	finished restoring m101.funnynumbers (100 documents)
2016-02-15T23:30:23.349+0000	done
$ mongo
MongoDB shell version: 3.2.0
connecting to: test
> use m101
switched to db m101
> db.hw1.findOne()
{
	"_id" : ObjectId("50773061bf44c220307d8514"),
	"answer" : 42,
	"question" : "The Ultimate Question of Life, The Universe and Everything"
}
```
