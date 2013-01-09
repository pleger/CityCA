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

#executing the main method of the code
automaton = Automaton(ROWS,COLUMNS)
analyzer = Analyzer(automaton)
automaton.createPopulation(POPULATION,Agent.randomRangeRadiumUnif(1,5))

simulation = Simulation(automaton, True)
simulation.start(ITERATIONS)
rankings = analyzer.getRankingOfPopulation()
print analyzer.getLinearRegressionData(False)

