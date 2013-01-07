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
ITERATIONS = 40


class TestFitness(unittest.TestCase):

    def setUp(self):
        self.grid = Automaton(ROWS,COLUMNS)
        self.simulation = Simulation(self.grid, False)


    def test_default(self):

        self.grid.reinit(ROWS,COLUMNS)
        self.grid.createPopulation(POPULATION,Agent.infiniteRadium())
        self.simulation.start(ITERATIONS)
        self.assertTrue(self.grid.convergence,"IT IS CONVERGENCE")
        array = self.grid.getMatrixOfPopulation()
        self.assertEqual(array.max(), len(self.grid.getAgents()), "ONE PLACE")

    def test_random(self):

        self.grid.reinit(ROWS,COLUMNS)
        self.grid.createPopulation(POPULATION,Agent.infiniteRadium(), Agent.randomFitness)
        self.simulation.start(ITERATIONS)
        self.assertFalse(self.grid.convergence,"IT IS NOT CONVERGENCE")


if __name__ == '__main__':
    unittest.main()

