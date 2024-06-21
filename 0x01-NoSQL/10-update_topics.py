#!/usr/bin/env python3
'''Python function to update the 'topics' field in school documents based on the provided name.'''

def modify_school_topics(mango_collection, name, topics):
    '''Update the 'topics' field of all documents in a MongoDB collection '''
    mango_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

