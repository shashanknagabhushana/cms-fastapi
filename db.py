from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["cms_database"]
content_collection = db["content_items"]
