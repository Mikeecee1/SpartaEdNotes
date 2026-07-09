import pymongo

print("Starting...")

client = pymongo.MongoClient("mongodb://localhost:27017/")

print("Connected")

print(client.list_database_names())

print("Finished")