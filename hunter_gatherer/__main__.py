#Run Application
from scraper import CarScrape
import sys


def main():
    try:
        website = sys.argv[1]
        website = website.decode('base64', 'strict')
        carscrape = CarScrape("jaguar", "f-pace", website)
        carscrape.getallurls()
        for car in carscrape.urls:
            print car
    except IndexError:
        print "Please enter a valid, encoded website"
        print "Key is available on request from the developer."
    except:
        print "Un-decodable website key. Please check key is correct and " \
              "try again. If problem pursues, contact developer directly."


if __name__ == '__main__':
    main()