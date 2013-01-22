"""
This class is used to test the project. Apart from the class, this file contains a script to execute the project.
This script should always be executed before to commit/push a change
TODO: Add more tests
"""

import unittest
from Agent import Agent
from Automaton import Automaton
from Simulation import Simulation


COLUMNS = 10
ROWS = 10
POPULATION = 30
ITERATIONS = 20


class TestFitness(unittest.TestCase):

    def setUp(self):
        self.automaton = Automaton(ROWS,COLUMNS)
        self.simulation = Simulation(self.automaton, False)


    def test_population(self):

        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.createPopulation(POPULATION,Agent.infiniteRadium())
        self.simulation.start(ITERATIONS)
        self.assertTrue(self.automaton.convergence,"IT IS CONVERGENCE")
        array = self.automaton.getMatrixOfPopulation()
        #print repr(self.automaton) + " " + repr(array.max())
        self.assertEqual(POPULATION, len(self.automaton.getAgents()), "ALL AGENTS")

    def test_default(self):

        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.createPopulation(POPULATION,Agent.infiniteRadium())
        self.simulation.start(ITERATIONS)
        self.assertTrue(self.automaton.convergence,"IT IS CONVERGENCE")
        array = self.automaton.getMatrixOfPopulation()
        #print repr(self.automaton) + " " + repr(array.max())
        self.assertEqual(array.max(), len(self.automaton.getAgents()), "ONE PLACE")


    def test_random(self):

        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.createPopulation(POPULATION,Agent.infiniteRadium(), Agent.randomFitness)
        self.simulation.start(ITERATIONS)
        self.assertFalse(self.automaton.convergence," IT IS NOT CONVERGENCE")


if __name__ == '__main__':
    unittest.main()

