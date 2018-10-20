from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
from pyorbital import tlefile
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from OrbitalPlotter import OrbitalPlotter

if __name__ == '__main__':
    filename = "data/named_sample_tles_master.txt"
    obp = OrbitalPlotter(filename)
    obp.initialize("11U","12U")
    obp.plot()