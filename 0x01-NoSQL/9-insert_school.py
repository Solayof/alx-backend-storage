#!/usr/bin/env python3
"""Python function that inserts a new document in a collection kwargs"""


def insert_school(mongo_collection, **kwargs):
    """insert kwargs into db"""
    return mongo_collection.insert_one(kwargs).inserted_id
