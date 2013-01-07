"""
This script is used to execute the cellular automaton Chile
"""

from Automaton import Automaton
from Simulation import Simulation
from Analyzer import Analyzer
from Agent import Agent

#TODO: USE A GUI TO CONFIG THESE PARAMETERS
COLUMNS = 30
ROWS = 30
POPULATION = 120
ITERATIONS = 20
Simulation.DEBUG_ITERATIONS = 5

#executing the main method of the code
grid = Automaton(ROWS,COLUMNS)
analyzer = Analyzer(grid)
grid.createPopulation(POPULATION,Agent.randomUnifRangeRadium(1,5))

simulation = Simulation(grid, ITERATIONS, True)
simulation.start()
rankings = analyzer.getRankingOfPopulation()
print analyzer.getLinearRegressionData(False)

