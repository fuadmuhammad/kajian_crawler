# Scrapy settings for radiorodja project
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

BOT_NAME = 'radiorodja'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['radiorodja.spiders']
NEWSPIDER_MODULE = 'radiorodja.spiders'
DEFAULT_ITEM_CLASS = 'radiorodja.items.RadiorodjaItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

