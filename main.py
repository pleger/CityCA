"""
This script is used to execute the cellular automaton Chile
"""

from Automaton import Automaton
from Simulation import Simulation
from Analyzer import Analyzer
from Agent import Agent

#TODO: USE A GUI TO CONFIG THESE PARAMETERS
COLUMNS = 10
ROWS = 10
POPULATION = 30
ITERATIONS = 40

#executing the main method of the code
grid = Automaton(ROWS,COLUMNS)
analyzer = Analyzer(grid)
grid.createPopulation(POPULATION,Agent.randomUnifRangeRadium(1,5))

simulation = Simulation(grid, True)
simulation.start(ITERATIONS)
rankings = analyzer.getRankingOfPopulation()
print analyzer.getLinearRegressionData()

#print rankings

