### SPACEJAM.PY ###

### LIBRARIES ###
from pyorbital.orbital import Orbital
import datetime
import numpy as np

### GLOBAL CONSTANTS ###

### GLOBAL FUNCTIONS ###

def segment_tle_list(filename):
	fp = open(filename,'r')

def next_tle(filepointer):
	x = list()
	for i in range(3):
		x.append(filepointer.readline())
	return x

def compare_orbits(orbit_A, orbit_B):
	return
### CLASSES ###

class Orbit(Orbital):
	'''Wrapper class for the pyorbital.orbital.Orbital class plus additional methods.'''
	#(r,v)=ISS.get_position(now,False)
	def angular_momentum(self,dt):
		(r,v)=self.get_position(dt,False) 	#r is radius vector in meters and v is velocity vector in km/s.
		self.h = np.cross(r,v*1000) 		#h is angular momentum vector in m^2/s

	def _compute_orbital_parameters(self):
		self.Omega = self.tle.right_ascension
		self.i = self.tle.inclination
		self.e = self.tle.excentricity
		self.omega = self.tle.arg_perigee
		self.M = self.tle.mean_anomaly
	def _compute_period(self):
		self.period = datetime.timedelta(minutes=self.orbit_elements.period)
		return self.period.total_seconds()


### END OF SPACEJAM.PY ###