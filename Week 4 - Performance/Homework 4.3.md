####### Homework: Homework 4.3

NOTE there is a bug [(TOOLS-939)](https://jira.mongodb.org/browse/TOOLS-939?_ga=1.214964948.233411772.1455713353) affecting some versions of mongoimport and mongorestore that causes ``mongoimport -d blog -c posts < posts.json`` to fail. As a workaround, you can use ``mongoimport -d blog -c posts < posts.json --batchSize 1``.

**Making the Blog fast**

Please download hw4-3.zip from the [Download Handout](https://university.mongodb.com/static/MongoDB_2016_M101P_January/handouts/hw4-3.4b679bd3844f.zip) link to get started. This assignment requires Mongo 3.0 or above.

In this homework assignment you will be adding some indexes to the post collection to make the blog fast.

We have provided the full code for the blog application and you don't need to make any changes, or even run the blog. But you can, for fun.

We are also providing a patriotic (if you are an American) data set for the blog. There are 1000 entries with lots of comments and tags. You must load this dataset to complete the problem.

From the mongo shell:

```
use blog
db.posts.drop()
```

From the mac or PC terminal window

``
mongoimport -d blog -c posts < posts.json
``

The blog has been enhanced so that it can also display the top 10 most recent posts by tag. There are hyperlinks from the post tags to the page that displays the 10 most recent blog entries for that tag. (run the blog and it will be obvious)

Your assignment is to make the following blog pages fast:

* The blog home page
* The page that displays blog posts by tag (http://localhost:8082/tag/whatever)
* The page that displays a blog entry by permalink (http://localhost:8082/post/permalink)
* By fast, we mean that indexes should be in place to satisfy these queries such that we only need to scan the number of documents we are going to return.

To figure out what queries you need to optimize, you can read the blog.py code and see what it does to display those pages. Isolate those queries and use explain to explore.

Once you have added the indexes to make those pages fast run the following.

``
python validate.py
``

(note that for folks who are using MongoLabs or MongoHQ there are some command line options to validate.py to make it possible to use those services) Now enter the validation code below.

##### Answer: 893jfns29f728fn29f20f2

The blog home page

```
> db.posts.createIndex( { date : -1 } )
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}
```

The page that displays blog posts by tag (http://localhost:8082/tag/whatever)
```
> db.posts.createIndex( { permalink : 1 } )
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 2,
	"numIndexesAfter" : 3,
	"ok" : 1
}
```

The page that displays a blog entry by permalink (http://localhost:8082/post/permalink)
```
> db.posts.createIndex( { tags : 1, date : -1 } )
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 3,
	"numIndexesAfter" : 4,
	"ok" : 1
}
```

Run validate.py
```
python validate.py
Welcome to the HW 4.3 Checker. My job is to make sure you added the indexes
that make the blog fast in the following three situations
	When showing the home page
	When fetching a particular post
	When showing all posts for a particular tag
Data looks like it is properly loaded into the posts collection
Home page is super fast. Nice job.

Blog retrieval by permalink is super fast. Nice job.

Blog retrieval by tag is super fast. Nice job.

Tests Passed for HW 4.3. Your HW 4.3 validation code is 893jfns29f728fn29f20f2
```
