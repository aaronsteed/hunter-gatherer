#Run Application
from scraper import CarScrape
import json

def main():
    carscrape = CarScrape("jaguar", "f-pace")
    carscrape.getallurls()
    for car in carscrape.urls:
        print car
