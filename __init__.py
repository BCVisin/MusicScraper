from scrapers import run_scraper
from google_play_music import search
from google_play_music import playlists
from datetime import date
import argparse

from pprint import pprint

def main(scraper='klove', playlist_name=''):

	stats = {}

	playlist_name = playlist_name or '%s-%s' % (scraper, date.today())
	print 'Building playlist %s' % (playlist_name,)

	playlist_object = playlists.playlist()
	playlist_id = playlist_object.get_or_create_playlist_id(name=playlist_name)
	stats['playlist'] = {'id':playlist_id, 'name':playlist_name}

	items = run_scraper.run_scraper(scraper=scraper)
	stats['songs'] = {'scraped_count': len(items), 'added_count':0, 'added_ids':[], 'added_items':[], 'skipped_count':0, 'skipped_items':[]}
	play_search = search.search()
	for item in items:
		search_results = play_search.search_item(item)
		song_nid = play_search.score_threashold(results=search_results)

		if song_nid:
			song_id = playlist_object.add_song(song_nid, playlist_id, skip_if_exists=True)
		else:
			song_id = None

		if song_id:
			stats['songs']['added_count'] += 1
			stats['songs']['added_ids'].append(song_id)
			stats['songs']['added_items'].append(item)
		else:
			stats['songs']['skipped_count'] += 1
			stats['songs']['skipped_items'].append(item)

	return stats

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Scrape a page and build a playlist off the scraped page')

	parser.add_argument('-s', '--scraper', type=str, default='klove', help='The scraper we want to crawl. Default is klove')
	parser.add_argument('-p', '--playlist_name', type=str, default='', help='The name of the playlist.  It will default to the scraper name + todays date')

	args = parser.parse_args()
	args = vars(args)

	stats = main(**args)

	print 'Playlist Name: %s' % stats['playlist']['name']

	print '----------------------------------------------'
	print 'Songs Added: %s' % stats['songs']['added_count']
	for song in stats['songs']['added_items']:
		print '%s by %s' % (song.get('title'), song.get('artist'))

	print '----------------------------------------------'
	print 'Songs Skipped: %s' % stats['songs']['skipped_count']
	for song in stats['songs']['skipped_items']:
		print '%s by %s' % (song.get('title'), song.get('artist'))

	print '----------------------------------------------'
	print 'Scraped: %s | Added: %s | Skipped: %s' % (stats['songs']['scraped_count'], stats['songs']['added_count'], stats['songs']['skipped_count'])



