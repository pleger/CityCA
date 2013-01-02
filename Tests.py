"""
This class is used to test the project. Apart from the class, this file contains a script to execute the project.
This script should always be executed before to commit/push a change
TODO: Add more tests
"""

import unittest
from Agent import Agent
from Grid import Grid
from Simulation import Simulation
from numpy import random


COLUMNS = 10
ROWS = 10
POPULATION = 30
ITERATIONS = 40


class TestFitness(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(ROWS,COLUMNS)
        self.simulation = Simulation(self.grid, False)


    def test_default(self):
        RADIUS = -1
        self.grid.clear()
        self.grid.createPopulation(POPULATION,RADIUS)
        self.simulation.start(ITERATIONS)
        self.assertTrue(self.grid.convergence,"IT IS CONVERGENCE")
        array = self.grid.getMatrixOfPopulation()
        self.assertEqual(array.max(), len(self.grid.getAgents()), "ONE PLACE")

    def test_random(self):

        RADIUS = -1
        self.grid.clear()
        self.grid.createPopulation(POPULATION,RADIUS, Agent.randomFitness)
        self.simulation.start(ITERATIONS)
        self.assertFalse(self.grid.convergence,"IT IS CONVERGENCE")


if __name__ == '__main__':
    unittest.main()

