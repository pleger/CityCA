"""
This script is used to execute the cellular automaton Chile
"""

from Automaton import Automaton
from Simulation import Simulation
from Analyzer import Analyzer

#TODO: USE A GUI TO CONFIG THESE PARAMETERS
COLUMNS = 10
ROWS = 10
POPULATION = 30
ITERATIONS = 40
RADIUS = 2

#executing the main method of the code
grid = Automaton(ROWS,COLUMNS)
analyzer = Analyzer(grid)
grid.createPopulation(POPULATION,RADIUS)

simulation = Simulation(grid, True)
simulation.start(ITERATIONS)
rankings = analyzer.getRankingOfPopulation()
print rankings

