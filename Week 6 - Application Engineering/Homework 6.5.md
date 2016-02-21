##### Homework: Homework 6.5

In this homework you will build a small replica set on your own computer. We will check that it works with validate.py, which you should download from the [Download Handout](https://university.mongodb.com/static/MongoDB_2016_M101P_January/handouts/validate.dcea5a51b377.py) link.

Create three directories for the three mongod processes. On unix, this could be done as follows:

``
mkdir -p /data/rs1 /data/rs2 /data/rs3
``

Now start three mongo instances as follows. Note that are three commands. The browser is probably wrapping them visually.

```
mongod --replSet m101 --logpath "1.log" --dbpath /data/rs1 --port 27017 --smallfiles --oplogSize 64 --fork

mongod --replSet m101 --logpath "2.log" --dbpath /data/rs2 --port 27018 --smallfiles --oplogSize 64 --fork

mongod --replSet m101 --logpath "3.log" --dbpath /data/rs3 --port 27019 --smallfiles --oplogSize 64 --fork
```

Windows users: Omit *-p* from *mkdir*. Also omit *--fork* and use *start mongod* with Windows compatible paths (i.e. backslashes "\") for the *--dbpath* argument (e.g; *C:\data\rs1*).

Now connect to a mongo shell and make sure it comes up
``
mongo --port 27017
``

Now you will create the replica set. Type the following commands into the mongo shell:
```
config = { _id: "m101", members:[
          { _id : 0, host : "localhost:27017"},
          { _id : 1, host : "localhost:27018"},
          { _id : 2, host : "localhost:27019"} ]
};
rs.initiate(config);
```

At this point, the replica set should be coming up. You can type
``
rs.status()
``

to see the state of replication.

Now run validate.py to confirm that it works.
``
python validate.py
``

Validate connects to your local replica set and checks that it has three nodes. It has been tested under Pymongo 2.3 and 2.4. Type the validation code below.

#####Answer: kjvjkl3290mf0m20f2kjjv

Start instance 1:

```
$ mongod --replSet m101 --logpath "1.log" --dbpath /data/rs1 --port 27017 --smallfiles --oplogSize 64 --fork
about to fork child process, waiting until server is ready for connections.
forked process: 2940
child process started successfully, parent exiting
```

Start instance 2:

```
$ mongod --replSet m101 --logpath "2.log" --dbpath /data/rs2 --port 27018 --smallfiles --oplogSize 64 --fork
about to fork child process, waiting until server is ready for connections.
forked process: 2964
child process started successfully, parent exiting
```

Start instance 3:

```
$ mongod --replSet m101 --logpath "3.log" --dbpath /data/rs3 --port 27019 --smallfiles --oplogSize 64 --fork
about to fork child process, waiting until server is ready for connections.
forked process: 2992
child process started successfully, parent exiting

```

Create the replica set

```
mongo --port 27017
MongoDB shell version: 3.2.0
connecting to: 127.0.0.1:27017/test
Server has startup warnings:
2016-02-21T03:49:14.074+0000 I CONTROL  [initandlisten] ** WARNING: You are running this process as the root user, which is not recommended.
2016-02-21T03:49:14.074+0000 I CONTROL  [initandlisten]
> config = { _id: "m101", members:[
...           { _id : 0, host : "localhost:27017"},
...           { _id : 1, host : "localhost:27018"},
...           { _id : 2, host : "localhost:27019"} ]
... };
{
 "_id" : "m101",
 "members" : [
   {
     "_id" : 0,
     "host" : "localhost:27017"
   },
   {
     "_id" : 1,
     "host" : "localhost:27018"
   },
   {
     "_id" : 2,
     "host" : "localhost:27019"
   }
 ]
}
> rs.initiate(config);
{ "ok" : 1 }

m101:OTHER> rs.status()
{
 "set" : "m101",
 "date" : ISODate("2016-02-21T03:53:56.500Z"),
 "myState" : 2,
 "term" : NumberLong(0),
 "heartbeatIntervalMillis" : NumberLong(2000),
 "members" : [
   {
     "_id" : 0,
     "name" : "localhost:27017",
     "health" : 1,
     "state" : 2,
     "stateStr" : "SECONDARY",
     "uptime" : 283,
     "optime" : {
       "ts" : Timestamp(1456026830, 1),
       "t" : NumberLong(-1)
     },
     "optimeDate" : ISODate("2016-02-21T03:53:50Z"),
     "infoMessage" : "could not find member to sync from",
     "configVersion" : 1,
     "self" : true
   },
   {
     "_id" : 1,
     "name" : "localhost:27018",
     "health" : 1,
     "state" : 2,
     "stateStr" : "SECONDARY",
     "uptime" : 6,
     "optime" : {
       "ts" : Timestamp(1456026830, 1),
       "t" : NumberLong(-1)
     },
     "optimeDate" : ISODate("2016-02-21T03:53:50Z"),
     "lastHeartbeat" : ISODate("2016-02-21T03:53:55.479Z"),
     "lastHeartbeatRecv" : ISODate("2016-02-21T03:53:53.478Z"),
     "pingMs" : NumberLong(0),
     "configVersion" : 1
   },
   {
     "_id" : 2,
     "name" : "localhost:27019",
     "health" : 1,
     "state" : 2,
     "stateStr" : "SECONDARY",
     "uptime" : 6,
     "optime" : {
       "ts" : Timestamp(1456026830, 1),
       "t" : NumberLong(-1)
     },
     "optimeDate" : ISODate("2016-02-21T03:53:50Z"),
     "lastHeartbeat" : ISODate("2016-02-21T03:53:55.480Z"),
     "lastHeartbeatRecv" : ISODate("2016-02-21T03:53:53.464Z"),
     "pingMs" : NumberLong(0),
     "configVersion" : 1
   }
 ],
 "ok" : 1
}
```

Run Validate.py

```
$ python validate.py
Welcome to the HW 6.x replica Checker. My job is to make sure you started a replica set with three nodes
Looks good. Replica set with three nodes running
Tests Passed for HW 6.5. Your HW 6.5 validation code is kjvjkl3290mf0m20f2kjjv
```
