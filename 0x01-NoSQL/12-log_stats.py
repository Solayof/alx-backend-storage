#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB:"""
from pymongo import MongoClient


client = MongoClient()
db = client.logs

print(db.nginx.estimated_document_count(), "logs")
print("Methods:")

for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    print(f"\tmethod {method}: {db.nginx.count_documents({'method': method})}")

count = db.nginx.count_documents(
    {"method": "GET", "path": "/status"}
    )
print(count, "status", "check")
