from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
from pyorbital import tlefile
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from OrbitalPlotter import OrbitalPlotter, Orbit

if __name__ == '__main__':
    filename = "data/named_sample_tles_master.txt"
    orbital_names = ["11U","12U","16U"]
    orbits = []
    for orb in orbital_names:
        orbits.append(Orbit(orb,filename))
    obp = OrbitalPlotter(orbits)
    obp.plot()
    #print( obp.get_orbital_position(obp.orbital1))