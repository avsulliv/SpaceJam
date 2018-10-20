from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
from pyorbital import tlefile
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class OrbitalPlotter:
    def __init__(self, file):
        self.file = file
        self.file2 = file
        self.orbital1 = None
        self.orbital2 = None
        self.o1_xyz = [[],[],[]]
        self.o2_xyz = [[],[],[]]

    def initialize(self, sat_1_name, sat_2_name):
        self.orbital1 = Orbital(sat_1_name,self.file)
        self.orbital2 = Orbital(sat_2_name,self.file2)
    
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        now = datetime.now()
        for i in range(0,2000):
            now += timedelta(seconds=4)
            position = self.orbital1.get_position(now,False)
            position2 = self.orbital2.get_position(now,False)
            for i in range(0,3):
                self.o1_xyz[i].append(position[0][i])
                self.o2_xyz[i].append(position2[0][i])
        ax.scatter(self.o1_xyz[0], self.o1_xyz[1], self.o1_xyz[2], c='r', marker='o')
        ax.scatter(self.o2_xyz[0], self.o2_xyz[1], self.o2_xyz[2], c='b', marker='o')
        plt.show()

if __name__ == '__main__':
    filename = "data/named_sample_tles_master.txt"
    obp = OrbitalPlotter(filename)
    obp.initialize("11U","12U")
    obp.plot()