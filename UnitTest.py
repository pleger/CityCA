__author__ = 'pleger'

import unittest
from Grid import Grid
from Simulation import Simulation

COLUMNS = 10
ROWS = 10
POPULATION = 30
ITERATIONS = 40
RADIUS = -1


class TestFitness(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(ROWS,COLUMNS)
        self.simulation = Simulation(self.grid, animation = False)


    def test_defaultFitness(self):
        self.grid.createPopulation(POPULATION,RADIUS)
        self.simulation.start(ITERATIONS)
        self.assertTrue(self.grid.isConvergence(),"IT IS CONVERGENCE")
        array = self.grid.getMatrixOfPopulation()
        self.assertEqual(array.max(), len(self.grid.getAgents()), "ONE PLACE")

if __name__ == '__main__':
    unittest.main()

