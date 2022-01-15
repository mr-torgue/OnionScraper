# OnionScraper
Scrapes data dumps for onion links! From websites like gist.github.com and pastebin.

# Pre-requisites
Python3 and scrapy. On Ubuntu this can be installed by 'sudo apt install python3 python3-scrapy'.

# Usage
OnionScraper can be run with 'scrapy crawl onion'. This will run the spider only once.
To deploy a spider follow: https://docs.scrapy.org/en/latest/topics/deploy.html. Or just add a simple cronjob.

# Improvements
This is a simple but working concept. Currently it is only checking for onion addresses in two sources (pastebin and github gist). OnionScaper can be improved by looking for more types of data, like ip adresses or URL's. 
