#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout, ConnectionError
import json
from scraper import Scraper


class URLScraper(Scraper):
    def __init__(self, make_of_car, model_of_car, url, regex):
        Scraper.__init__(self, make_of_car, model_of_car, url, regex)
        self._links = []

    def __iter__(self):
        return iter(self._links)

    def get_urls_for_page(self, html):
        regex = self._regex
        urls = []
        soup = BeautifulSoup(html, 'html.parser')
        try:
            script_tag = soup.find("script", {"id": "data"})
            regex_found_data = regex.findall(str(script_tag))[0]
            json_data = json.loads(regex_found_data)["results"]
        except AttributeError:
            return False

        for i, car in enumerate(json_data):
            if i > 1:
                urls.append(car["url"])
            else:
                pass

        self._links = self._links + urls
        if len(urls) == 0:
            return False
        else:
            return True

    def get_all_urls(self):
        i = 1
        try:
            # time.sleep(6)  # Don't want to hammer those servers!
            request = requests.get('http://' + self._url +
                                   '/search/result/cars' +
                                   '/make/' + self._make_of_car + '/model/' +
                                   self._model_of_car + '/page/' + str(i) +
                                   '/limit/30')
            has_data = self.get_urls_for_page(request.content)
            while has_data:
                i += 1
                request = requests.get('http://' + self._url +
                                       '/search/result/' +
                                       'cars/make/' + self._make_of_car +
                                       '/model/' +
                                       self._model_of_car + '/page/' +
                                       str(i) + '/limit/30')
                has_data = self.get_urls_for_page(request.content)

        except (ConnectionError, Timeout):
            # TODO Logging and better error messages
            print("Error")
