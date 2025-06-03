from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://edward:sonbn123456789@witty-coder.mz8yewk.mongodb.net/book_db?retryWrites=true&w=majority&appName=witty-coder"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print("Connection error:", e)

db = client["book_db"]
collection = db["books"]   
users_collection = db["users"]   