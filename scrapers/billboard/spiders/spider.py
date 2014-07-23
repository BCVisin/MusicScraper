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

	name = "billboard"
	allowed_domains = ["billboard.com"]
	start_urls = ["http://www.billboard.com/charts/christian-songs", "http://www.billboard.com/charts/christian-songs?page=1", "http://www.billboard.com/charts/christian-songs?page=2"]

	def parse_start_url(self, response):

		sel = Selector(response)
		for row in sel.xpath('//article[contains(@class, "chart_albumTrack_detail")]'):

			item = ItemLoader(item=song(), selector=row)

			item.add_value('request_page', response.url)
			item.add_xpath('title', "header/h1/text()")
			item.add_xpath('artist', "header/p/a/text()")

			loaded_item = item.load_item()

			yield loaded_item
