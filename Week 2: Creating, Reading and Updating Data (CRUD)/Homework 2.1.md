###### Homework: Homework 2.1

In this problem, you will be using a collection of student scores that is similar to what we used in the lessons. Please download grades.json from the Download Handout link and import it into your local mongo database as follows:

``
$ mongoimport -d students -c grades < grades.json
``

The dataset contains 4 scores for 200 students.

First, let’s confirm your data is intact; the number of documents should be 800.
```
use students
db.grades.count()
```

You should get 800.

This next query, which uses the aggregation framework that we have not taught yet, will tell you the student_id with the highest average score:

```
> db.grades.aggregate(
    {'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}},
    {'$sort':{'average':-1}},
    {'$limit':1}
  )
```

The answer should be student_id 164 with an average of approximately 89.3.

Now it’s your turn to analyze the data set. Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest.

What is the student_id of the lowest exam score above 65?

###### Answer: 22

```
$ mongoimport -d students -c grades < grades.json
2016-02-15T23:46:15.872+0000	connected to: localhost
2016-02-15T23:46:16.026+0000	imported 800 documents
```

```
$ mongo
MongoDB shell version: 3.2.0
connecting to: test
> use students
switched to db students
> db.grades.count()
800
> db.grades.aggregate(
    {
      '$match': { 'score':{ $gte: 65} }
    },
    {
      '$sort':{'score':1}
    },
    {
      '$limit':1
    }
  )
{ "_id" : ObjectId("50906d7fa3c412bb040eb5cf"), "student_id" : 22, "type" : "exam", "score" : 65.02518811936324
```
