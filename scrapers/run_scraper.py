from twisted.internet import reactor
from importlib import import_module

from scrapy.crawler import Crawler
from scrapy import signals
from scrapy.settings import CrawlerSettings

def run_scraper(scraper):

	settings_module = import_module('scrapers.%s.settings' % scraper)
	spider_module = import_module('scrapers.%s.spiders.spider' % scraper)
	spider = spider_module.Spider()
	settings = CrawlerSettings(settings_module)
	items = []

	def _item_passed(item):
		items.append(item)

	crawler = Crawler(settings)
	crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
	crawler.signals.connect(_item_passed, signal=signals.item_passed)
	crawler.configure()
	crawler.crawl(spider)

	crawler.start()
	reactor.run()

	return items
