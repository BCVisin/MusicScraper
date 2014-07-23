from gmusicapi import Mobileclient
import conf

class GoogleCommon(object):

	def __init__(self, username=conf.GOOGLE_USERNAME, password=conf.GOOGLE_PASSWORD, **kwargs):

		self.mobile_api = Mobileclient()
		self.logged_in = self.login(username, password)

	def login(self, username, password):
		"""use this method to log in.  Should be handleded by the __init__ but in case we need to re-authenticate, it's here"""
		self.logged_in = self.mobile_api.login(username, password)
		return self.logged_in
