from pyorbital.orbital import Orbital
from datetime import datetime, timedelta
from pyorbital import tlefile
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Orbit:
    def __init__(self,name,file):
        self.file = file
        self.orbital = Orbital(name,file)
        self.xyz=[[],[],[]]
        self.now = datetime.now()
        self.position = self.orbital.get_position(self.now,False)
        for i in range(0,2000):
            self.now += timedelta(seconds=4)
            position = self.orbital.get_position(self.now,False)
            for i in range(0,3):
                self.xyz[i].append(position[0][i])
                
    def get_x(self):
        return self.xyz[0]
    def get_y(self):
        return self.xyz[1]
    def get_z(self):
        return self.xyz[2]

class OrbitalPlotter:
    def __init__(self, orbs):
        self.orbitals = orbs

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        color = 
        for item in self.orbitals:
            ax.scatter(item.get_x(), item.get_y(), item.get_z(), c='r', marker='o')
        plt.show()
