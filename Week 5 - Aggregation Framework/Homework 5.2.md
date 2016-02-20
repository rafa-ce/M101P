##### Homework: Homework 5.2 (Hands On)

**Crunching the Zipcode dataset**
Please calculate the average population of cities in California (abbreviation CA) and New York (NY) (taken together) with populations over 25,000.

For this problem, assume that a city name that appears in more than one state represents two separate cities.

Please round the answer to a whole number.
Hint: The answer for CT and NJ (using this data set) is 38177.

Please note:
* Different states might have the same city name.
* A city might have multiple zip codes.

For purposes of keeping the Hands On shell quick, we have used a subset of the data you previously used in zips.json, not the full set. This is why there are only 200 documents (and 200 zip codes), and all of them are in New York, Connecticut, New Jersey, and California.

If you prefer, you may [download the handout](https://university.mongodb.com/static/MongoDB_2016_M101P_January/handouts/small_zips.0e6e16620617.zip) and perform your analysis on your machine with

``
> mongoimport -d test -c zips --drop small_zips.json
``

Once you've generated your aggregation query and found your answer, select it from the choices below.

#####Answer: 44804


```
> db.zips.aggregate(
  {
    $group:{_id:{city:'$city',state:'$state'}, population:{$sum:'$pop'}}
  },
  {
    $match: { $or:[{"_id.state":'CA'},{"_id.state":'NY'}], population: { $gt: 25000 } }
  },
  {
    $group:{_id:null,avg:{$avg:'$population'}}
  }
)
{ "_id" : null, "avg" : 44804.782608695656 }

```
