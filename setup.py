from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hunter-gatherer',
    version='2.0.0-Snapshot-5',

    description='A gathering and machine-learning system for AutoGrab.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/aaronsteed/hunter-gatherer',

    # Author details
    author='Aaron Steed',
    author_email='aaron.steed2@mail.dcu.ie',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.6',
    ],
    data_files=[
        ('/etc/init.d', ['data/scripts/hunter-gatherer']),
        ('/usr/share/hunter-gatherer',
         ['data/conf/hunter-gatherer.conf.example'])
    ],
    keywords='scraping parsing machine-learning',
    packages=find_packages(exclude=['resources']),
    install_requires=['requests', 'BeautifulSoup4', 'pymongo'],

    entry_points={
        'console_scripts': [
            'hunter-gatherer=hunter_gatherer.__main__:main',
        ],
    },
)
