""" This is the class we will use to search google music."""
from . import GoogleCommon

class playlist(GoogleCommon):
	"""playlist classs"""

	def __init__(self, *args, **kwargs):

		super(playlist, self).__init__(*args, **kwargs)

		self.current_playlist = {}

	def get_all_playlists(self):
		"""wrapper to get all the playlists"""

		return self.mobile_api.get_all_user_playlist_contents()


	def get_playlist(self, name=None, playlist_id=None):
		"""get a playlist by name or ID"""

		all_playlists = self.get_all_playlists()
		for playlist_result in all_playlists:
			if name and playlist_result.get('name') == name:
				self.current_playlist = playlist_result
				return playlist_result
			elif id and playlist_result.get('id') == playlist_id:
				self.current_playlist = playlist_result
				return playlist_result

		return False

	def get_or_create_playlist_id(self, name):
		"""this method will get a playlist by name, or create a new one, set it to the current playlist, and then return the playlist id"""

		returned_playlist = self.get_playlist(name=name)
		if returned_playlist:
			return returned_playlist.get('id')
		else:
			new_playlist_id = self.mobile_api.create_playlist(name=name)
			self.get_playlist(playlist_id=id)
			return new_playlist_id

	def add_song(self, song_id, playlist_id, skip_if_exists=True):
		"""add a song to a playlist and optionally skip if it already exists in that playlist which is the default"""

		if skip_if_exists:
			if not self.current_playlist.get('id') == playlist_id:
				self.get_playlist(playlist_id)

			for song in self.current_playlist.get('tracks', []):
				if song.get('trackId') == song_id or song.get('track', {}).get('nid') == song_id or song.get('storeId') == song_id:
					return False

		return self.mobile_api.add_songs_to_playlist(playlist_id=playlist_id, song_ids=song_id)

