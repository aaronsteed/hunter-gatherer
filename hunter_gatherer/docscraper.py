#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from scraper import Scraper
import json
import re
import time

def convert_list_of_maps_to_map(list_of_maps):
    converted_map = {}
    for map in list_of_maps:
        for k,v in map.items():
            converted_map[k] = v

    return converted_map


class DocScraper(Scraper):
    def __init__(self, make_of_car, model_of_car, url, regex):
        Scraper.__init__(self, make_of_car, model_of_car, url, regex)
        self._data = {}

    def _format_price(self):
        money_regex = re.compile('&euro;(.*)')
        amount_in_euros = money_regex.findall(self._data[2]
                                              ["Price"][0]
                                              ["eur"])[0]
        self._data[2]["Price"] = amount_in_euros

    def get_data_of_url(self):
        try:
            time.sleep(6)  # Don't want to hammer those servers
            html = requests.get(self._url).content
            soup = BeautifulSoup(html, 'html.parser')
            script_tag = soup.find("script", {"id": "data"})
            regex_found_data = self._regex.findall(str(script_tag))[0]
            self._data = \
                json.loads(regex_found_data)["result"]["factSheetDetails"]
            self._format_price()
            self._data = convert_list_of_maps_to_map(self._data)
        except ConnectionError:
            # TODO Logging and better error messages
            print("Error")

    def get_data(self):
        return self._data
