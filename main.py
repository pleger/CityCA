__author__ = '''Paul Leger'''

from Grid import Grid
from Simulation import Simulation
import numpy as np

#TODO: USE A GUI TO CONFIG THESE PARAMETERS
COLUMNS = 10
ROWS = 10
POPULATION = 30
ITERATIONS = 40
RADIUS = 2

if __name__ == "__main__":
    grid = Grid(ROWS,COLUMNS)
    grid.createPopulation(POPULATION,RADIUS)

    simulation = Simulation(grid)
    simulation.start(ITERATIONS)
    rankings = grid.getRankingOfPopulation()
    print rankings