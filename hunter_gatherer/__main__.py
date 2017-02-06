#!/usr/bin/env python
from database import HunterDB
import sys
import re
from urlscraper import URLScraper
from docscraper import DocScraper
from base64 import b64decode


def main():
    try:
        website = bytes(sys.argv[1], 'utf-8')
        website = (b64decode(website)).decode('utf-8')
        regex = re.compile('.*window.jsonData=(.*);</script>')
        docregex = re.compile('.*window.jsonData=(.*)</script>')
        cars_scrape = URLScraper("jaguar",
                                 "f-pace",
                                 website,
                                 regex)
        cars_scrape.get_all_urls()
        docscraper = DocScraper("jaguar",
                                "f-pace",
                                cars_scrape.links[0],
                                docregex)
        docscraper.get_data_of_url()
        db = HunterDB()
        db.post_to_db(docscraper)
    except IndexError:
        print("Please enter a valid, encoded website url")
        print("Key is available on request from the developer.")


if __name__ == '__main__':
    main()
