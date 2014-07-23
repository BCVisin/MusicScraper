from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector

from scrapy.contrib.loader import ItemLoader

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst

class song(Item):

	"""This is the base item for a song"""

	request_page = Field(output_processor=TakeFirst())

	title = Field(output_processor=TakeFirst())
	album = Field(output_processor=TakeFirst())
	artist = Field(output_processor=TakeFirst())

class Spider(CrawlSpider):

	name = "klove"
	allowed_domains = ["klove.com"]
	start_urls = ["http://www.klove.com/music/songs/new-songs.aspx"]

	def parse_start_url(self, response):

		sel = Selector(response)
		for row in sel.xpath('//table/tr'):
			if not row.xpath('td'):
				continue

			item = ItemLoader(item=song(), selector=row)

			item.add_value('request_page', response.url)
			item.add_xpath('title', 'td[3]/a[1]/text()')
			item.add_xpath('artist', 'td[3]/a[2]/text()')
			item.add_xpath('album', 'td[4]/text()')



			loaded_item = item.load_item()

			yield loaded_item
