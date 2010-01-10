# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import csv

class KajianPipeline(object):
    def __init__(self):
      self.csvwriter = csv.writer(open('items.csv', 'wb'))

    def process_item(self, domain, item):
	link_lowercase = item['link_lowercase'][0].replace('%20',' ')
#	desc = item['description'][0].replace("\n","")
	self.csvwriter.writerow([item['link'], item['title'][0], link_lowercase])
        return item
