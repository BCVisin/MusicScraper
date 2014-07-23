""" This is the class we will use to search google music."""
from . import GoogleCommon

class search(GoogleCommon):
	"""search classs"""

	def search_item(self, item):
		"""given a scrapy item, search for it and return the song_id"""

		search_results = self.search(song=item.get('title'), artist=item.get('artist'), album=item.get('album'))
		return search_results


	def search(self, song, artist=None, album=None):
		"""use this method to search for a song"""

		search_string = song

		if artist:
			search_string = '%s by %s' % (song, artist)

		result = self.mobile_api.search_all_access(query=search_string)

		return result

	def score_threashold(self, results):
		"""look at the results and only return the nid of the song if we believe it is the correct song"""

		for result in results.get('song_hits', []):
			if result.get('score') > 100:
				return result.get('track', {}).get('nid')
			else:
				return False
