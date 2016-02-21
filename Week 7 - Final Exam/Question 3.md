#####Final: Question 3

In this problem you will update a document in the Enron dataset (which can be found [here](https://s3.amazonaws.com/edu-downloads.10gen.com/enron/enron.zip)) to illustrate your mastery of updating documents from the shell.

Please add the email address "mrpotatohead@mongodb.com" to the list of addresses in the "headers.To" array for the document with "headers.Message-ID" of "<8147308.1075851042335.JavaMail.evans@thyme>"

After you have completed that task, please download final3-validate-mongo-shell.js from the [Download Handout](https://university.mongodb.com/static/MongoDB_2016_M101P_January/handouts/final3-validate-mongo-shell.98637d16fdd8.js) link and run

``
mongo final3-validate-mongo-shell.js
``

to get the validation code and put it in the box below without any extra spaces. The validation script assumes that it is connecting to a simple mongo instance on the standard port on localhost.

#####Answer: vOnRg05kwcqyEFSve96R

```
> db.messages.update(
   { "headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>"},
   { $push: { "headers.To": "mrpotatohead@mongodb.com"} }
)
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

Run final3-validate-mongo-shell.js:

```
$ mongo final3-validate-mongo-shell.js
MongoDB shell version: 3.2.0
connecting to: test
Welcome to the Final Exam Q3 Checker. My job is to make sure you correctly updated the document
Final Exam Q3 Validated successfully!
Your validation code is: vOnRg05kwcqyEFSve96R
```
