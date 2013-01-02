"""
This script is used to execute the cellular automata
"""

__author__ = '''Paul Leger'''

from Grid import Grid
from Simulation import Simulation
from Analyzer import Analyzer

#TODO: USE A GUI TO CONFIG THESE PARAMETERS
COLUMNS = 10
ROWS = 10
POPULATION = 30
ITERATIONS = 40
RADIUS = 2

if __name__ == "__main__":
    grid = Grid(ROWS,COLUMNS)
    analyzer = Analyzer(grid)
    grid.createPopulation(POPULATION,RADIUS)

    simulation = Simulation(grid, True)
    simulation.start(ITERATIONS)
    rankings = analyzer.getRankingOfPopulation()
    print rankings