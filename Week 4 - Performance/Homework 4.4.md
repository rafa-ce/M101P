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
