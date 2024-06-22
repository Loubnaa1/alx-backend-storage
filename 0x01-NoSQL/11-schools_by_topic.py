#!/usr/bin/env python3
""" Returning the list of school having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """  Returning the list of school having a specific topic."""
    topic = {'topics': topic}
    return [doc for doc in mongo_collection.find(topic)]
