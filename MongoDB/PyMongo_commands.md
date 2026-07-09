# PyMongo Cheat Sheet

## Connect to MongoDB

``` python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["starwars"]
characters = db["characters"]
```

Remote server:

``` python
client = MongoClient("mongodb://<server>:27017")
```

------------------------------------------------------------------------

## Find Documents

``` python
for doc in characters.find():
    print(doc)
```

Find one:

``` python
luke = characters.find_one({"name": "Luke Skywalker"})
print(luke)
```

Nested field:

``` python
for doc in characters.find({"homeworld.name": "Mon Cala"}):
    print(doc["name"])
```

Projection:

``` python
for doc in characters.find(
    {},
    {"_id": 0, "name": 1, "gender": 1}
):
    print(doc)
```

------------------------------------------------------------------------

## Count

``` python
characters.count_documents({})
characters.count_documents({"gender": "female"})
```

------------------------------------------------------------------------

## Sort

``` python
from pymongo import ASCENDING, DESCENDING

for doc in characters.find().sort("name", ASCENDING):
    print(doc["name"])

for doc in characters.find().sort("height", DESCENDING):
    print(doc["name"], doc["height"])
```

------------------------------------------------------------------------

## Limit & Skip

``` python
characters.find().limit(5)

characters.find().skip(10).limit(5)
```

------------------------------------------------------------------------

## Insert

``` python
characters.insert_one({
    "name": "Grogu",
    "species": "Unknown"
})
```

``` python
characters.insert_many([
    {"name": "Luke"},
    {"name": "Leia"}
])
```

------------------------------------------------------------------------

## Update

``` python
characters.update_one(
    {"name": "Luke Skywalker"},
    {"$set": {"rank": "Jedi Master"}}
)
```

``` python
characters.update_many(
    {"gender": "male"},
    {"$set": {"alive": True}}
)
```

------------------------------------------------------------------------

## Delete

``` python
characters.delete_one({"name": "Grogu"})
characters.delete_many({"gender": "unknown"})
```

------------------------------------------------------------------------

## Distinct

``` python
characters.distinct("gender")
characters.distinct("homeworld.name")
```

------------------------------------------------------------------------

## Regular Expressions

``` python
characters.find({
    "name": {"$regex": "^L"}
})

characters.find({
    "name": {"$regex": "sky", "$options": "i"}
})
```

------------------------------------------------------------------------

## Comparison Operators

``` python
characters.find({"height": {"$gt": 180}})
characters.find({"height": {"$lt": 170}})
characters.find({"height": {"$gte": 180}})
characters.find({"height": {"$lte": 180}})
characters.find({"gender": {"$ne": "male"}})
```

------------------------------------------------------------------------

## Logical Operators

``` python
characters.find({
    "$or": [
        {"gender": "male"},
        {"gender": "female"}
    ]
})
```

AND is implicit:

``` python
characters.find({
    "gender": "male",
    "eye_color": "blue"
})
```

------------------------------------------------------------------------

## Import JSON

``` python
import json

with open("starWars.characters.json") as f:
    docs = json.load(f)

characters.insert_many(docs)
```

------------------------------------------------------------------------

## Aggregation

``` python
pipeline = [
    {"$match": {"gender": "male"}},
    {"$group": {"_id": "$homeworld.name", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]

for doc in characters.aggregate(pipeline):
    print(doc)
```

------------------------------------------------------------------------

# mongosh vs PyMongo

  mongosh              PyMongo
  -------------------- ---------------------
  `find()`             `find()`
  `findOne()`          `find_one()`
  `insertOne()`        `insert_one()`
  `insertMany()`       `insert_many()`
  `updateOne()`        `update_one()`
  `updateMany()`       `update_many()`
  `deleteOne()`        `delete_one()`
  `deleteMany()`       `delete_many()`
  `countDocuments()`   `count_documents()`
  `aggregate()`        `aggregate()`
  `distinct()`         `distinct()`

## Learning Path

1.  Connect to MongoDB
2.  Find / find_one
3.  Projection
4.  Sort / limit / skip
5.  Insert
6.  Update
7.  Delete
8.  Aggregation
9.  Indexes
