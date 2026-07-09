import pymongo


# Connect to your local MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select a database and a collection (MongoDB creates these automatically if they don't exist)
db = client["test_database"]
collection = db["test_collection"]

# Insert a single document
mock_data = {"item": "canvas", "qty": 100, "status": "active"}
insert_result = collection.insert_one(mock_data)
print(f"Document inserted with ID: {insert_result.inserted_id}")

# Fetch and print the document back out
found_document = collection.find_one({"item": "canvas"})
print(f"Retrieved from MongoDB: {found_document}")
