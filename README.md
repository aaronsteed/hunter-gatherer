[![Stories in Ready](https://badge.waffle.io/aaronsteed/hunter-gatherer.png?label=ready&title=Ready)](https://waffle.io/aaronsteed/autograb-backend)
# AutoGrab-Backend
<img src="https://github.com/aaronsteed/autograb-backend/raw/master/resources/static/images/logo.png" alt="alt text" width="200" height="200" style="display:inline;">

> AutoGrab-Backend is a service which gathers car data and performs machine learning techniques to predict cars of a good price.
This program is intended to be used by the autograb-frontend service.

### Prerequisites 
Requires the following: 
- Ubuntu 12.04 or greater
- [Python](https://www.python.org/downloads/)
    - [Pip]([Python](https://www.python.org/downloads/))
    - PyMongo
    - BeautifulSoup4
    - Requests
    - Scikit-Learn
- MongoDB 
- Ruby, Gem
- Make
- gcc

---
### Local Installation ###
 
 - Install [Mongo DB](https://docs.mongodb.com/manual/installation/) and run service on standard port.
 - Download the source in ether a .zip or tar.gz format. Unzip appropriately.
 - Navigate to the source file and type the following : 
    - ```python setup.py install```
    - ```pip install -r requirements.txt```
 - Note: It is recommended you install all applications in a ```virtualenv```  
 - Now that the application is installed, there are two ways to run the application, 
in the foreground, or in the background (daemon)
    - To run the application as a daemon service, one must change the init script to be executable. (Only if installed via ```setuptools```)
        - ```sudo chmod +x /etc/init.d/hunter-gatherer```
        - ```sudo service autograb-backend start```
    - If installed via dpkg using a deb file, all post install requirements are fulfilled.
        - ```sudo service autograb-backend start```
 - To run the application in the foreground, simply type ```autograb-backend```
 
---
### Development ###


- Clone the repo ```git clone git@github.com:aaronsteed/autograb-backend.git```
- Submit pull requests to master branch
 
---
### Deployment ###

##### Creation #####
 - To create a deb package from the following software :
    - Ensure all packages for deployment are met :
        - ```sudo apt-get install ruby ruby-dev gem gcc make```
    - Install fpm : 
        - ```sudo gem install fpm```
    - Ensure python is installed and that the default python is ```python3```. If ```/usr/bin/python``` is not 
    ```python3```, there are two options : 
        - Create a ```virtualenv``` of ```python3``` and activate it. ```python``` will now default to ```python3```
        - Delete symlink to ```python2``` and create a new link pointing to ```python3```.      
        E.g.      
        ```sudo rm -r /path/to/python/symlink```      
        ```ln -s /path/to/python3 /usr/bin/python```
    - Install ```pip3```
        - ```sudo apt-get install python3-pip```
        - If failed may require ```sudo apt-get update``` and a rerun of the above command. 
    - Like ```python```, ensure the symlink ```pip``` points to ```pip3``` and not ```pip2``` or otherwise. Two options : 
        - Create a ```virtualenv``` of ```python3``` and activate it. ```pip``` will now default to ```pip3```
        - Delete symlink to ```pip``` and create a new link pointing to ```pip3```.   
        E.g.        
        ```sudo rm -r /path/to/pip/symlink```                 
        ```ln -s /path/to/pip3 /usr/bin/pip```
    - Note : Do the latter of each of these steps at your own risk.
    - Create deb of package :
        - ```fpm --no-dependencies --deb-no-default-config-files --after-install resources/scripts/after_install -s python -t deb setup.py```
        - This will create a package "python-autograb-backend_x.x.x.all.deb"
    - Install requirements of application : 
        - ```sudo pip install -r /usr/share/autograb-backend/requirements.txt```
    - Application is now ready to be run as a daemon or forefround process.


##### Installation #####
 - To install deb on the Ubuntu 12.04 or greater machine : 
    - ```sudo dpkg -i python-autograb-backend_x.x.x.all.deb```
 
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
    - ```Pip``` : Dependency management.
    - ```PyMongo``` : Database driver for MongoDB
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
