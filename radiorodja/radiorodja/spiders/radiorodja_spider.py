from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from radiorodja.items import RadiorodjaItem

class RadiorodjaSpider(CrawlSpider):
    domain_name = "radiorodja.com"
    start_urls = [
        "http://www.radiorodja.com",
    ]
    
    rules = (
        Rule(SgmlLinkExtractor(allow_domains='radiorodja.com',unique=True),follow=True,callback='parse_item'),
    )

    def parse_item(self, response):
      hxs = HtmlXPathSelector(response)
      items = []
      item = RadiorodjaItem()
      item['link'] = response.url
      href = hxs.select('//div[@class="podPress_content"]/a[4]/@href').extract()
      item['link_lowercase'] = href
      text = hxs.select('//div[@class="PostHead"]/h1/text()').extract() 
      item['title']=text
      desc1 = hxs.select('//div[@class="PostContent"]/p[1]/text()').extract()
      item['desc1']=desc1
      desc2 = hxs.select('//div[@class="PostContent"]/p[2]/text()').extract()
      item['desc2']=desc2
      desc3 = hxs.select('//div[@class="PostContent"]/p[3]/text()').extract()
      item['desc3']=desc3
      desc4 = hxs.select('//div[@class="PostContent"]/p[4]/text()').extract()
      item['desc4']=desc4
      items.append(item)
      return items
        
SPIDER = RadiorodjaSpider()
