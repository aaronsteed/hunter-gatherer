#!/usr/bin/env python

# Format for URL of website :
# http://www.website.country/search/result/cars/make/make_of_car/model/model_of_car/page/n/limit/30
from bs4 import BeautifulSoup
import requests
import re
import json


class CarScrape:
    def __init__(self, make_of_car, model_of_car):
        self.soup = BeautifulSoup
        self.regex = re.compile('.*window.jsonData=(.*);</script>')
        self.make_of_car = make_of_car
        self.model_of_car = model_of_car
        self.urls = []

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
                print price
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
        request = requests.get('http://website/search/result/cars/'
                               'make/' + self.make_of_car + '/model/' +
                               self.model_of_car + '/page/' + str(i) +
                               '/limit/30')
        json_data = self.geturlsforpage(request.content)
        print json_data
        while json_data:
            i += 1
            request = requests.get('http://website/search/result/cars/'
                                   'make/' + self.make_of_car + '/model/' +
                                   self.model_of_car + '/page/' + str(i) +
                                   '/limit/30')
            json_data = self.geturlsforpage(request.content)
