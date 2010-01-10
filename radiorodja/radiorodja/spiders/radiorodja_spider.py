from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from kajian.items import KajianItem

class RadiorodjaSpider(CrawlSpider):
    domain_name = "radiorodja.com"
    start_urls = [
        "http://radiorodja.com",
    ]
    
    rules = (
        Rule(SgmlLinkExtractor(allow_domains='kajian.net',unique=True),follow=True,callback='parse_item'),
    )

    def parse_item(self, response):
      hxs = HtmlXPathSelector(response)
      links = hxs.select('//div[@class="post"]')
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

      return items
        
SPIDER = RadiorodjaSpider()
