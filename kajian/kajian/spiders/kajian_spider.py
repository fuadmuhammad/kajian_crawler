#from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from kajian.items import KajianItem

class KajianSpider(CrawlSpider):
    domain_name = "kajian.net"
    start_urls = [
        "http://kajian.net/kajian-audio/Ceramah",
    ]
    
    rules = (
        Rule(SgmlLinkExtractor(allow_domains='kajian.net',unique=True),follow=True,callback='parse_item'),
    )

    def parse_item(self, response):
      hxs = HtmlXPathSelector(response)
      links = hxs.select('//tr[@class="row0"]')
#      desc = hxs.select('//div[@class="zina-content clear-block"]/div[@class="section"][1]').extract()
      items = []
      for link in links:
	item = KajianItem()
	href = link.select('td[@class="song0 nowrap"]/a[2]/@href').extract()
	item['link_lowercase'] = href
	item['link'] = response.url
	text = link.select('td[@class="song0 fullwidth"]/a/text()').extract() 
        item['title']=text
#	item['description']=desc
        items.append(item)

      links = hxs.select('//tr[@class="row1"]')
      for link in links:
	item = KajianItem()
	href = link.select('td[@class="song1 nowrap"]/a[2]/@href').extract()
	item['link_lowercase'] = href
	item['link'] = response.url
	text = link.select('td[@class="song1 fullwidth"]/a/text()').extract() 
        item['title']=text
        items.append(item)

      return items
        
SPIDER = KajianSpider()
