# Scrapy settings for kajian project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'kajian'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['kajian.spiders']
NEWSPIDER_MODULE = 'kajian.spiders'
DEFAULT_ITEM_CLASS = 'kajian.items.KajianItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = ['kajian.pipelines.KajianPipeline']
