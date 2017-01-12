
import keyring
import getpass

class Authenticator(object):
	api = None
	domain = None
	email = None

	def __init__(self, domain, email, api):
		self.email = email
		self.domain = domain
		self.api = api

	def authenticate(self):
		while not self.email:
			self.email = raw_input('Please enter your login email: ')
		
		auth_token = keyring.get_password(self.domain, self.email)
		password = None

		while not auth_token:
			while not password:
				print "Didn't found previous authentications, type your password. (It's not stored locally)"
				password = getpass.getpass()
				if not password:
					print "Password can't be empty"

			try:
				auth_token = self.api.request_auth_token(email=self.email, password=password)
			except:
				pass

			if not auth_token:
				print "Not authenticated. (Did not receive valid authentication token.)"
				password = ''
			else:
				keyring.set_password(self.domain, self.email, auth_token)

		return auth_token
