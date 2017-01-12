
from training import Training

class PredefinedTrainings(object):
	@staticmethod
	def pompeczki(count):
		pompki = Training(count / 6.0, 46, 0.0)
		pompki.name = "Pompki " + str(count)
		return pompki

	@staticmethod
	def hiking(time_in_minutes, distance):
		hike = Training(time_in_minutes, 16, distance)
		hike.name = "Hiking for " + str(time_in_minutes) + " minutes"
		return hike

	@staticmethod
	def biking(time_in_minutes, distance):
		bike = Training(time_in_minutes, 1, distance)
		bike.name = "Bike for " + str(time_in_minutes) + " minutes"
		return bike
