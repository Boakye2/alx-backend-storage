#!/usr/bin/env python3
""" Pymongo """


def list_all(mongo_collection: object) -> list:
    """List all documents in a collection

    Args:
        mongo_collection (object):
        pymongo collection object
    """
    return mongo_collection.find({}) if mongo_collection.find({}) else []
