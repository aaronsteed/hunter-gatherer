[![Stories in Ready](https://badge.waffle.io/aaronsteed/hunter-gatherer.png?label=ready&title=Ready)](https://waffle.io/aaronsteed/hunter-gatherer)
# Hunter-Gatherer
<img src="https://github.com/aaronsteed/hunter-gatherer/raw/master/resources/static/images/logo.png" alt="alt text" width="200" height="200" style="display:inline;">

> Hunter-Gatherer is a service which seeks and gathers car data and performs machine learning on its data. 

### Requirements
Requires the following: 
- Ubuntu 12.04 or greater
- [Python](https://www.python.org/downloads/)
    - [Pip]([Python](https://www.python.org/downloads/))
    - Supervisor
    - BeautifulSoup4
    - Requests
    - Scikit-Learn
- MongoDB 

---
### Installation ###
 
 - Download the source in ether a .zip or tar.gz format. Unzip appropriately.
 - Navigate to the source file and type the following : 
    - ```python setup.py install```
 - Now that the application is installed, there are two ways to run the application, 
in the foreground, or in the background (daemon)
 - To run the application as a saemon service, one must chnage the init scrpt to be executable. 
    - ```sudo chmod +x /etc/init.d/hunter-gatherer```
 - To run the application in the foreground, simply type ```hunt```
 
---
### Development ###

 - Clone the repo ```git clone git@github.com:aaronsteed/hunter-gatherer.git```
 - Submit pull requests to master branch
 
---
### Todos ###

 - Machine learning module of project. :chart_with_upwards_trend:
 - Integration with autograb-frontend. :zap:
 - Complete deployment/local installation environment. :outbox_tray:
 
---
### Technologies Used
- Python 
    - ```Requests``` : Access web sites via HTTP.
    - ```BeautifulSoup4``` : HTML and XML Parsing. 
    - ```Scikit-learn``` : Machine-learing algorithms on data.
    - ```Supervisor``` : Daemonization of program and monitoring of proccesses. 
    - ```Pip``` : Dependency management.
- MongoDB : Storage of data.
- Travis CI : Continuous Integration

---
### Version
**2.0**

---
License
---

MIT
**Free Software, Hell Yeah!**

This file was generated on Fri 16 Dec 2016 02:29:15 GMT
