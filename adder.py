# source: https://github.com/isoteemu/sports-tracker-liberator

from endomondo import MobileApi, Workout
from datetime import datetime, timedelta, date, time
from rc_helpers.training import Training
from rc_helpers.authentication import Authenticator
from rc_helpers.config import PredefinedTrainings

# set it to predefine your email
email = None

if __name__ == '__main__':
	endomondoapi = MobileApi()
	authenticator = Authenticator("endomodno", email, endomondoapi)
	auth_token = authenticator.authenticate()
	endomondoapi.set_auth_token(auth_token)

	used_training = PredefinedTrainings.biking(22.0, 5.1)
	
	print "You picked: " + str(used_training)

	workout = Workout()
	workout.name = used_training.name
	workout.sport = int(used_training.type)
	workout.duration = int(used_training.duration_minutes * 60)
	workout.start_time = datetime.utcnow() - timedelta(days=used_training.days_ago) - timedelta(seconds=workout.duration)
	workout.distance = used_training.distance # workout.duration*0.0027777778

	print "Adding ..."
	
	endomondoapi.post_workout(workout=workout, properties={'audioMessage': 'false'})
	if workout.id:
		print 'Saved! Reloading...'
		reload = endomondoapi.get_workout(workout)
		print 'Burned '  + str(reload.calories) + ' calories on ' + reload.name
