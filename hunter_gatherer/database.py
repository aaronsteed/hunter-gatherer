#!/usr/bin/env python
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from datetime import datetime


class HunterDB:
    def __init__(self):
        try:
            client = MongoClient(host='localhost',
                                 port=27017)
            self._client = client
        except ServerSelectionTimeoutError:
            print("Database not running or could be using a different port or \
            IP address")

    def post_to_db(self, doc_scraper):
        db = self._client["Hunter-Gatherer-DB"]
        collection = db[doc_scraper.get_make_of_car()]
        post = doc_scraper.get_data()
        post['created'] = datetime.utcnow()
        collection.insert_one(post)






