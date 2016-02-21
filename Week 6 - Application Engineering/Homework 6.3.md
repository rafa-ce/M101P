##### Homework: Homework 6.3

Which of the following statements are true about choosing and using a shard key?

:white_check_mark: There must be a index on the collection that starts with the shard key.

:white_medium_square: You can change the shard key on a collection if you desire.

:white_medium_square: The shard key must be unique

:white_check_mark: MongoDB can not enforce unique indexes on a sharded collection other than the shard key itself, or indexes prefixed by the shard key.

:white_check_mark: Any update that does not contain the shard key will be sent to all shards.

#####Answer

Let's look at each of those statements:

"The shard key must be unique" This is not true. You can have a shard key that is not unique, though you should still consider issues of shard key cardinality (how granular it is) and selectivity (how many individual documents a query using the shard key would bring back).

"There must be a index on the collection that starts with the shard key." This is true. If you start with an empty collection, MongoDB will put that index in the collection for you. If the collection has data in it and you try to shard on a particular key, it will expect the index to be there, or the creation of the shard key will fail.

"MongoDB can not enforce unique indexes on a sharded collection other than the shard key itself, or indexes prefixed by the shard key." And that is true. An index that doesn't start with the shard key can't be enforced for uniqueness. This actually comes up if you decide to shard on a key other than the *_id* key, because the *_id* key must be unique. But Mongo can't help you keep it unique, because if two documents had the same *_id* they might still live on different shards. And so it's your responsibility to keep it unique. This is not usually a big deal if you're letting the *_id* be an auto-generated ObjectId, because the system does a good job of generating those uniquely. But if you decide to, let's say, shard on something other than the *_id*, and you also specify the *_id* field manually, then it's up to you to keep it unique or bad things will happen.

"Any update that does not contain the shard key will be sent to all shards." So that is absolutely true. The database, if it does not get the shard key in the query, will need to send the query to all the shards. So keep that in mind.

"You can change the shard key on a collection if you desire." Absolutely false. It's quite permanent and immutable. You cannot change a shard key on a collection. And if you want to change a shard key on a collection, you would have to essentially dump data, re-import it in some way into a new collection with a new shard key, which would be painful.
