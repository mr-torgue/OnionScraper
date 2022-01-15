import scrapy
import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from onion_scraper.items import OnionItem
'''
We call this the onion spider but the extraction of onion links is not done here.
Crawler extracts links from 2 sources github gist and pastebin. It ignores the next page and only allows same domain.
For each page found a item is made (also nothing todo with extracting onion addresses)
'''
class OnionSpider(CrawlSpider):
    name = "onion"
    allowed_domains = ['pastebin.com', 'gist.github.com']
    start_urls = [
        'https://pastebin.com/archive',
        'https://gist.github.com/discover'
    ]
    # crawl every item on archive not going to another archive
    rules = (
        Rule(LinkExtractor(deny=('/archive/.*', ), restrict_xpaths="//table[contains(@class, 'maintable')]"), callback='parse_page_pastebin'),
        Rule(LinkExtractor(deny=('/discover/.*', ), restrict_xpaths="//a[contains(@class, 'link-overlay')]"), callback='parse_page_github_gist'),
    )

    def parse_page_pastebin(self, response):
        self.logger.info('Found %s ...', response.url)
        origin = "pastebin"
        text = response.xpath("//textarea[contains(@class, 'textarea')]/text()").get()
        title = response.xpath("//div[contains(@class, 'info-top')]/h1/text()").get()
        creation_date = response.xpath("//div[contains(@class, 'date')]/span/@title").get()
        yield OnionItem(title=title, text=text, creation_date=creation_date, origin=origin)

    '''
    Use contains
    '''
    def parse_page_github_gist(self, response):
        self.logger.info('Found %s ...', response.url)
        origin = "github gist"
        # find raw page button by checking if it contains class btn-sm and text Raw
        raw_page = response.xpath("//a[contains(@class, 'btn-sm') and contains(text(), 'Raw')]/@href").get()
        if raw_page != None:
            # we are not yet in the raw page
            yield response.follow(raw_page, callback=self.parse_page_github_gist)
        else:
            # this is a raw page
            text = response.text
            title = response.url.split("/")[::-1]
            creation_date=datetime.datetime.now()
            yield OnionItem(title=title, text=text, creation_date=creation_date, origin=origin)
