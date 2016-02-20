####### Homework: Homework 4.4

In this problem you will analyze a profile log taken from a mongoDB instance. To start, please download sysprofile.json from [Download Handout](https://university.mongodb.com/static/MongoDB_2016_M101P_January/handouts/sysprofile.acfbb9617420.json) link and import it with the following command:

``
mongoimport -d m101 -c profile < sysprofile.json
``

Now query the profile data, looking for all queries to the students collection in the database school2, sorted in order of decreasing latency. What is the latency of the longest running operation to the collection, in milliseconds?

:white_medium_small_square: 19776550

:white_medium_small_square: 10000000

:white_medium_small_square: 5580001

:white_medium_small_square: 15820

:white_medium_small_square: 2350

##### Answer: 15820

```
$ mongo
MongoDB shell version: 3.2.0
connecting to: test
> use m101
switched to db m101
> db.profile.find({ op:"query", ns:/school2.students/}).sort({ millis: -1}).limit( 1)
{ "_id" : ObjectId("56c7a85f9411cf473ff3c91a"), "ts" : ISODate("2012-11-20T20:09:49.862Z"), "op" : "query", "ns" : "school2.students", "query" : { "student_id" : 80 }, "ntoreturn" : 0, "ntoskip" : 0, "nscanned" : 10000000, "keyUpdates" : 0, "numYield" : 5, "lockStats" : { "timeLockedMicros" : { "r" : 19776550, "w" : 0 }, "timeAcquiringMicros" : { "r" : 4134067, "w" : 5 } }, "nreturned" : 10, "responseLength" : 2350, "millis" : 15820, "client" : "127.0.0.1", "user" : "" }
```
