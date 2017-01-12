
from datetime import datetime, timedelta, date, time

class Training(object):
	name = "Training " + str(datetime.utcnow())
	duration_minutes = 0.0
	days_ago = 0
	type = 0
	distance = 0.0 # in km

	def __init__(self, minutes, type, distance):
		self.duration_minutes = minutes
		self.type = type
		self.distance = distance
	
	def __repr__(self):
		return "Training(" + name + ")"

	def __str__(self):
		return self.name + ", " + str(self.duration_minutes) + " minutes, " + str(self.distance) + " km, type: " + str(self.type)
