#!/usr/bin/env python
from pymongo import MongoClient
from datetime import datetime
import hashlib


class HunterDB:
    def __init__(self):
        self._client = MongoClient(host='localhost',
                                   port=27017)

    def post_to_db(self, doc_scraper):
        db = self._client["Hunter-Gatherer-DB"]
        collection = db[str(doc_scraper.get_make_of_car() +
                            "_" + doc_scraper.get_model_of_car())]
        document = doc_scraper.get_data()

        sha1_hash = hashlib.sha1()
        sha1_hash.update(document.__str__().encode('utf-8'))

        hexdigest = sha1_hash.hexdigest()
        document['created'] = datetime.utcnow()
        document['_id'] = hexdigest

        collection.find_one_and_update({'_id': hexdigest},
                                       {'$set': document},
                                       upsert=True)





