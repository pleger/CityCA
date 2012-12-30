
import unittest
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


    def test_defaul(self):
        RADIUS = -1
        self.grid.clear()
        self.grid.createPopulation(POPULATION,RADIUS)
        self.simulation.start(ITERATIONS)
        self.assertTrue(self.grid.isConvergence(),"IT IS CONVERGENCE")
        array = self.grid.getMatrixOfPopulation()
        self.assertEqual(array.max(), len(self.grid.getAgents()), "ONE PLACE")

    def test_random(self):
        def randomFitness(self,cell, own = False):
            return random.randint(30)

        RADIUS = -1
        self.grid.clear()
        self.grid.createPopulation(POPULATION,RADIUS,randomFitness)
        self.simulation.start(ITERATIONS)
        self.assertFalse(self.grid.isConvergence(),"IT IS CONVERGENCE")


if __name__ == '__main__':
    unittest.main()

