# OnionScraper
Scrapes data dumps for onion links from websites like gist.github.com and pastebin.com!

# Installation
You need Python installed. Following instructions are for linux. Installation in virtual environment to prevent interference.
* virtualenv -p /usr/bin/python3.8 .virtualenv
* source .virtualenv/bin/activate
* git clone https://github.com/mr-torgue/OnionScraper.git
* pip install scrapy
* cd OnionScraper

Replace python3.8 with your python installation. 

# Usage
Within the virtualenv. OnionScraper can be run with 'scrapy crawl onion'. This will run the spider only once.
You can deploy OnionScraper with scrapyd. For now you can run OnionScraper periodically using cron.
Add "15 * * * * [PATH]/.virtualenv/bin/scrapy crawl onion" to your crontab, this will make it run every 15 minutes. Can run as the user you installed virtualenv. as.

# Improvements
This is a simple but working concept. Currently it is only checking for onion addresses in two sources (pastebin and github gist). OnionScaper can be improved by looking for more types of data, like ip adresses or URL's. New sources could also be added. Because of it's design it does not receive updates, so it can miss certain posts. Could be prevented by adding logic to scrawl all new items.

* add duplicate detection.
* also include next page, continue until duplicate is reached.
* add feature for screenshots
* extend to more sources
* extend to more data types
* use scrapyd
