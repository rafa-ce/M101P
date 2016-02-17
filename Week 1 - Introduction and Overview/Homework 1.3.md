###### Homework: Homework 1.3

We are now going to test that you have bottle installed correctly and can run a bottle-based project. Download the handout and run it as follows:

``
$ python hw1-3.py
``

It requires that:

* bottle be installed correctly
* your mongodb to be running
* you have run mongorestore properly

From a different terminal window type the following from the command line: curl http://localhost:8080/hw1/50

Alternatively, you can put the url above into your web browser.

Type the two-digit answer into the box below (no spaces).

####### Answer: 53

Terminal 1:
```
$ python hw1-3.py
Bottle v0.12.9 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.

10.0.2.2 - - [10/Jan/2016 23:38:05] "GET /hw1/50 HTTP/1.1" 200 3
10.0.2.2 - - [10/Jan/2016 23:38:05] "GET /favicon.ico HTTP/1.1" 404 742
10.0.2.2 - - [10/Jan/2016 23:38:26] "GET /hw1/50 HTTP/1.1" 200 3
```

Terminal 2:
```
$ curl http://localhost:8080/hw1/50
53
```
