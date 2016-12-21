#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
import re
import json
import time


class CarScrape:
    def __init__(self, make_of_car, model_of_car, website):
        self.soup = BeautifulSoup
        self.regex = re.compile('.*window.jsonData=(.*);</script>')
        self.make_of_car = make_of_car
        self.model_of_car = model_of_car
        self.urls = []
        self.website = website

    def geturlsforpage(self, html):
        money_regex = re.compile('&euro;(\d*,\d*)')
        urls = []
        self.soup = self.soup(html, 'html.parser')
        try:
            script_tag = self.soup.find("script", {"id": "data"})
            car_data = self.regex.findall(str(script_tag))[0]
            json_data = json.loads(car_data)["results"]
        except AttributeError:
            return False

        for i, car in enumerate(json_data):
            if i > 1:
                price = money_regex.findall(str(car["price"][0]["eur"]))
                urls.append(car["url"])
            else:
                pass

        self.urls = self.urls + urls
        if len(urls) == 0:
            return False
        else:
            return True

    def getallurls(self):
        i = 1
        try:
            time.sleep(6) # Dont hammer those servers!
            request = requests.get('http://' + self.website + '/search/result/cars'
                                   '/make/' + self.make_of_car + '/model/' +
                                   self.model_of_car + '/page/' + str(i) +
                                   '/limit/30')
            has_data = self.geturlsforpage(request.content)
            while has_data:
                i += 1
                request = requests.get('http://' + self.website + '/search/result/'
                                       'cars/make/' + self.make_of_car + '/model/'
                                       + self.model_of_car + '/page/' +
                                       str(i) + '/limit/30')
                has_data = self.geturlsforpage(request.content)
        except ConnectionError:
            # TODO Add logging to application
            print "Error! Issue could be related to internet connection or " \
                  "website key is incorrect. Please consult both when " \
                  "troubleshooting."

    # def getcardata(self): # TODO this function
