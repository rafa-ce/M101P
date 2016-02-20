##### Homework: Homework 6.3

Which of the following statements are true about choosing and using a shard key?

:white_medium_small_square: There must be a index on the collection that starts with the shard key.

:white_medium_small_square: You can change the shard key on a collection if you desire.

:white_medium_small_square: The shard key must be unique

:white_medium_small_square: MongoDB can not enforce unique indexes on a sharded collection other than the shard key itself, or indexes prefixed by the shard key.

:white_medium_small_square: Any update that does not contain the shard key will be sent to all shards.
