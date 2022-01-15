import scrapy

'''
Defines the onion item. Item contains title, text content, creation date and origin (pastebin OR gist)
@TODO: naming is a bit ambigious, item contains all data onion address still needs to be extracted.
'''
class OnionItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    creation_date = scrapy.Field()
    origin = scrapy.Field()