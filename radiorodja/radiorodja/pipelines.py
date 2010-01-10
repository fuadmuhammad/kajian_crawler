# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import csv

class RadiorodjaPipeline(object):
    def __init__(self):
      self.csvwriter = csv.writer(open('items.csv', 'wb'))

    def process_item(self, domain, item):
	desc = str(item['desc1'][0].encode('utf-8'))+str(item['desc2'][0].encode('utf-8'))+str(item['desc3'][0].encode('utf-8'))+str(item['desc4'][0].encode('utf-8'))
	self.csvwriter.writerow([item['link'], item['title'][0],item['link_lowercase'][0],desc])
        return item
