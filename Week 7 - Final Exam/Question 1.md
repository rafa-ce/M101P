#####Final: Question 1

Please download the Enron email dataset [enron.zip](https://s3.amazonaws.com/edu-downloads.10gen.com/enron/enron.zip), unzip it and then restore it using mongorestore. It should restore to a collection called "messages" in a database called "enron". Note that this is an abbreviated version of the full corpus. There should be 120,477 documents after restore.

Inspect a few of the documents to get a basic understanding of the structure. Enron was an American corporation that engaged in a widespread accounting fraud and subsequently failed.

In this dataset, each document is an email message. Like all Email messages, there is one sender but there can be multiple recipients.

Construct a query to calculate the number of messages sent by Andrew Fastow, CFO, to Jeff Skilling, the president. Andrew Fastow's email addess was andrew.fastow@enron.com. Jeff Skilling's email was jeff.skilling@enron.com.

For reference, the number of email messages from Andrew Fastow to John Lavorato (john.lavorato@enron.com) was 1.

:white_medium_square: 1

:white_medium_square: 3

:white_medium_square: 5

:white_medium_square: 7

:white_medium_square: 9

:white_medium_square:12

#####Answer: 3

Run mongorestore:

```
$ mongorestore dump/
2016-02-21T21:56:13.314+0000	building a list of dbs and collections to restore from dump dir
2016-02-21T21:56:13.353+0000	reading metadata for enron.messages from
2016-02-21T21:56:13.380+0000	restoring enron.messages from
2016-02-21T21:56:16.351+0000	[####....................]  enron.messages  65.3 MB/377.9 MB  (17.3%)
2016-02-21T21:56:19.351+0000	[######..................]  enron.messages  105.7 MB/377.9 MB  (28.0%)
2016-02-21T21:56:22.351+0000	[#########...............]  enron.messages  147.1 MB/377.9 MB  (38.9%)
2016-02-21T21:56:25.420+0000	[##########..............]  enron.messages  172.8 MB/377.9 MB  (45.7%)
2016-02-21T21:56:28.352+0000	[#############...........]  enron.messages  209.1 MB/377.9 MB  (55.3%)
2016-02-21T21:56:31.367+0000	[##############..........]  enron.messages  231.1 MB/377.9 MB  (61.1%)
2016-02-21T21:56:34.352+0000	[################........]  enron.messages  255.8 MB/377.9 MB  (67.7%)
2016-02-21T21:56:37.420+0000	[#################.......]  enron.messages  272.3 MB/377.9 MB  (72.1%)
2016-02-21T21:56:40.359+0000	[#################.......]  enron.messages  277.7 MB/377.9 MB  (73.5%)
2016-02-21T21:56:43.351+0000	[##################......]  enron.messages  288.3 MB/377.9 MB  (76.3%)
2016-02-21T21:56:46.451+0000	[###################.....]  enron.messages  300.2 MB/377.9 MB  (79.4%)
2016-02-21T21:56:49.351+0000	[###################.....]  enron.messages  310.3 MB/377.9 MB  (82.1%)
2016-02-21T21:56:52.366+0000	[######################..]  enron.messages  351.4 MB/377.9 MB  (93.0%)
2016-02-21T21:56:55.022+0000	[########################]  enron.messages  377.9 MB/377.9 MB  (100.0%)
2016-02-21T21:56:55.022+0000	restoring indexes for collection enron.messages from metadata
2016-02-21T21:56:55.071+0000	finished restoring enron.messages (120477 documents)
2016-02-21T21:56:55.072+0000	done
```

Run query to calculate the number of messages sent by Andrew Fastow, CFO, to Jeff Skilling, the president:

```
db.messages.find(
  {
    "headers.From": "andrew.fastow@enron.com",
    "headers.To":"jeff.skilling@enron.com" }
  ).count();
```
