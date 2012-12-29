__author__ = '''Paul Leger'''

from Grid import Grid
from Simulation import Simulation
import numpy as np

#TODO: USE A GUI TO CONFIG THESE PARAMETERS
COLUMNS = 10
ROWS = 10
POPULATION = 30
ITERATIONS = 40
RADIUS = -1

def randomFitness(self,cell, own = False):
    return np.random.randint(20)

grid = Grid(ROWS,COLUMNS)
grid.createPopulation(POPULATION,RADIUS,randomFitness)


simulation = Simulation(grid)
simulation.start(ITERATIONS)
print grid   
