import json
import re

'''
Pipeline is exectued after an item has been scraped.
TODO: add feature for extracting more types of data
TODO: add duplicate filter
TODO: add feature for taking a screenshot
TODO: write data as json
'''
class OnionPipeline(object):

    def __init__(self):
        self.onionsfilename = "onionaddress.json"
        # simple onion regex
        self.onion_regex = re.compile("\w\+\.onion")
        #self.ipfilename = "ipaddress.json"
        #self.ip_regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        self.logfilename = "history.log"

    def open_spider(self, spider):
        self.onionfile = open(self.onionsfilename, 'w')
        #self.ipfile = open(self.ipfilename, 'w')
        self.logfile = open(self.logfilename, 'w')

    def close_spider(self, spider):
        self.onionfile.close()
        #self.ipfile.close()
        self.logfile.close()

    '''
    tries to find onion addresses by applying onion regex to contents.
    whole content is stored for logging purposes.
    '''
    def process_item(self, item, spider):
        self.logfile.write("Title: %s\nDate: %s\nOrigin: %s\nText: %s\n" % (str(item['title']), str(item['creation_date']), str(item['origin']), str(item['text'])))
        for onion in self.onion_regex.findall(item['text']):
            self.onionfile.write("%s\n" % (str(onion)))
        #for ip in self.ip_regex.findall(item['text']):
        #    self.ipfile.write("%s\n" % (str(ip)))
        return item
