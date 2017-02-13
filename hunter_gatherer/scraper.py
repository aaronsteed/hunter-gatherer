#!/usr/bin/env python

# Base Class for scrapers


class Scraper:
    def __init__(self, make_of_car, model_of_car, url, regex):
        self._make_of_car = make_of_car
        self._model_of_car = model_of_car
        self._url = url
        self._regex = regex

    def get_make_of_car(self):
        return self._make_of_car

    def get_model_of_car(self):
        return self._model_of_car

