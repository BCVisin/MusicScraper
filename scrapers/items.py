"""This file stores the default item classes that are common across all scrapers"""

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst

class song(Item):

	"""This is the base item for a song"""

	request_page = Field(output_processor=TakeFirst())

	title = Field(output_processor=TakeFirst())
	album = Field(output_processor=TakeFirst())
	artist = Field(output_processor=TakeFirst())
