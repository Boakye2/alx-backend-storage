#!/usr/bin/env python3
""" Top students """


def top_students(mongo_collection: object):
    """function that returns all students sorted by average score"""

    top = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top
