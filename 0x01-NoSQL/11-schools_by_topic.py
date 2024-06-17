#!/usr/bin/env python3
"""function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return list of school having a specific topic"""
    return [
        sch for sch in mongo_collection.find({"topics": topic})
    ]
