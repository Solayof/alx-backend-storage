#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """sort mongo collection"""
    return mongo_collection.aggregate([
        {
            "$project":
            {"name": "$name", "averageScore": {"$avg": "$topics.score"}}
            }, {"$sort": {"averageScore": -1}}
            ])
