# MongoDB `mongosh` Cheat Sheet

## Database Commands

``` javascript
show dbs
use starwars
db
db.dropDatabase()
```

## Collection Commands

``` javascript
show collections
db.createCollection("characters")
db.characters.drop()
```

## Insert

``` javascript
db.characters.insertOne({
  name: "Luke Skywalker",
  gender: "male"
})

db.characters.insertMany([
  {name:"Luke"},
  {name:"Leia"},
  {name:"Han"}
])
```

## Find

``` javascript
db.characters.find()
db.characters.findOne()

db.characters.find({
  gender: "male"
})

db.characters.find({
  "homeworld.name": "Mon Cala"
})
```

## Projection

``` javascript
db.characters.find(
  {},
  {
    _id: 0,
    name: 1,
    gender: 1
  }
)
```

## Count

``` javascript
db.characters.countDocuments()

db.characters.countDocuments({
  gender: "female"
})
```

## Comparison Operators

``` javascript
{$gt:180}
{$lt:170}
{$gte:180}
{$lte:180}
{$ne:"male"}
```

Example:

``` javascript
db.characters.find({
  height: {$gt:180}
})
```

## Logical Operators

### AND

``` javascript
db.characters.find({
  gender:"male",
  eye_color:"blue"
})
```

### OR

``` javascript
db.characters.find({
  $or:[
    {gender:"male"},
    {gender:"female"}
  ]
})
```

## Sorting

``` javascript
db.characters.find().sort({name:1})   // Ascending
db.characters.find().sort({name:-1})  // Descending
```

## Limit & Skip

``` javascript
db.characters.find().limit(5)
db.characters.find().skip(10)
```

## Update

``` javascript
db.characters.updateOne(
  {name:"Luke Skywalker"},
  {$set:{rank:"Jedi"}}
)

db.characters.updateMany(
  {gender:"male"},
  {$set:{alive:true}}
)
```

## Replace

``` javascript
db.characters.replaceOne(
  {name:"Luke Skywalker"},
  {
    name:"Luke",
    age:23
  }
)
```

## Delete

``` javascript
db.characters.deleteOne({
  name:"Luke Skywalker"
})

db.characters.deleteMany({
  gender:"unknown"
})
```

## Distinct Values

``` javascript
db.characters.distinct("gender")
db.characters.distinct("homeworld.name")
```

## Regular Expressions

``` javascript
db.characters.find({name:/^L/})
db.characters.find({name:/sky/i})
```

## Arrays

``` javascript
db.characters.find({
  "films.title":"A New Hope"
})
```

## Pretty Print

``` javascript
db.characters.find().pretty()
```

## Explain Query

``` javascript
db.characters.find({
  gender:"male"
}).explain()
```

## Help

``` javascript
db.help()
db.characters.help()
```

------------------------------------------------------------------------

# Most Useful Commands

  SQL             MongoDB
  --------------- -----------------------------
  SELECT \*       `find()`
  WHERE           Filter document in `find()`
  SELECT column   Projection
  ORDER BY        `sort()`
  LIMIT           `limit()`
  COUNT(\*)       `countDocuments()`
  INSERT          `insertOne()`
  UPDATE          `updateOne()`
  DELETE          `deleteOne()`

