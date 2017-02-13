#!/usr/bin/env python
from database import HunterDB
import time
import sys
import re
from urlscraper import URLScraper
from docscraper import DocScraper
from base64 import b64decode
from pymongo.errors import ServerSelectionTimeoutError


def run():
    try:
        website = bytes(sys.argv[1], 'utf-8')
        website = (b64decode(website)).decode('utf-8')
        url_regex = re.compile('.*window.jsonData=(.*);</script>')
        doc_regex = re.compile('.*window.jsonData=(.*)</script>')
        db = HunterDB()
        url_scraper = URLScraper("jaguar",
                                 "f-pace",
                                 website,
                                 url_regex)
        url_scraper.get_all_urls()
        for url in url_scraper:
            doc_scraper = DocScraper("jaguar",
                                     "f-pace",
                                     url,
                                     doc_regex)
            doc_scraper.get_data_of_url()
            db.post_to_db(doc_scraper)
    except ConnectionError:
        print("Check connection to the internet.")
    except IndexError:
        print("Please enter a valid, encoded website url")
        print("Key is available on request from the developer.")
    except ServerSelectionTimeoutError:
        print("Database not running or could be using a different port or "
              "IP address")


if __name__ == '__main__':
    start_time = time.time()
    run()
    print("Job completed in : " + str(time.time() - start_time))
