import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select database and collection
db = client["starWars"]
characters = db["characters"]

# Count documents
print(f"Number of characters: {characters.count_documents({})}")

# Find Ackbar
ackbar = characters.find_one({"name": "Ackbar"})

print(ackbar)

for character in characters.find({"homeworld.name": "Mon Cala"}):
    print(character["name"])
