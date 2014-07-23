# Scrapy settings for scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'klove'

SPIDER_MODULES = ['scrapers.klove.spiders.spider']
NEWSPIDER_MODULE = 'scrapers.klove.spiders.spider'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'MusicBot'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
