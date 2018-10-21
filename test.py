from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
from pyorbital import tlefile
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from OrbitalPlotter import OrbitalPlotter, Orbit

def getDistance(ISS,OTHER):
    max = 0
    result=[]
    for i in range(0,len(OTHER.xyz[0])):
        a = np.array( (ISS.xyz[0][i] , ISS.xyz[1][i] ,ISS.xyz[2][i]  ))
        b = np.array(  (OTHER.xyz[0][i] , OTHER.xyz[1][i] ,OTHER.xyz[2][i]  ))
        dist = np.linalg.norm(a-b)
        result.append(dist)
    print(result)
    print("satellite:" + OTHER.name)
    print(dist)

if __name__ == '__main__':
    filename = "data/named_sample_tles_master.txt"
    orbital_names = ["11U","204U","205U","631U","589U"]
    orbits = []
    for orb in orbital_names:
        orbits.append(Orbit(orb,filename))
    # obp = OrbitalPlotter(orbits)
    # obp.plot()

    ISS = Orbit("ISS",filename)

    for orbits in orbits:
        getDistance(ISS,orbits)

   

    #print( obp.get_orbital_position(obp.orbitorbital1))