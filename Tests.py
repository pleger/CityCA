"""
This class is used to test the project. Apart from the class, this file contains a script to execute the project.
This script should always be executed before to commit/push a change
TODO: Add more tests
"""

import unittest
from Agent import Agent
from Automaton import Automaton
from Simulation import Simulation


COLUMNS = 30
ROWS = 20
POPULATION = 30
ITERATIONS = 20


class TestFitness(unittest.TestCase):

    def setUp(self):
        self.automaton = Automaton(ROWS,COLUMNS)
        self.simulation = Simulation(self.automaton, False)

    def test_infiniteRadium(self):

        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.createPopulation(POPULATION,Agent.infiniteRadium())
        self.simulation.start(ITERATIONS)
        self.assertTrue(self.automaton.convergence,"IT IS CONVERGENCE")
        array = self.automaton.getMatrixOfPopulation()
        #print repr(self.automaton) + " " + repr(array.max())
        self.assertEqual(POPULATION, len(self.automaton.getAgents()), "ALL AGENTS")

    def test_withZeroRadium(self):
        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.createPopulation(POPULATION,Agent.constRadium(0))
        self.simulation.start(3)
        self.assertTrue(self.automaton.convergence,"IT IS CONVERGENCE")


    def test_random(self):

        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.createPopulation(POPULATION,Agent.infiniteRadium(), Agent.randomFitness)
        self.simulation.start(ITERATIONS)
        self.assertFalse(self.automaton.convergence," IT IS NOT CONVERGENCE")

    def test_circularRangeInf(self):
        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.enableCircularGrid()
        rr = [0,1,2,3,4,5,17,18,19]
        rc = [0,1,2,3,4,5,27,28,29]

        ranges = self.automaton.getRanges(1,1,4)
        ranges[0].sort()
        ranges[1].sort()

        self.assertEquals(rr,ranges[0],"Not same ranges for rows:"+repr(ranges[0]))
        self.assertEquals(rc,ranges[1],"Not same ranges for columns:"+repr(ranges[1]))


    def test_circularRangeSup(self):
        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.enableCircularGrid()
        rr = [0,1,2,14,15,16,17,18,19]
        rc = [0,1,23,24,25,26,27,28,29]

        ranges = self.automaton.getRanges(18,27,4)
        ranges[0].sort()
        ranges[1].sort()

        self.assertEquals(rr,ranges[0],"Not same ranges for rows:"+repr(ranges[0]))
        self.assertEquals(rc,ranges[1],"Not same ranges for columns:"+repr(ranges[1]))

    def test_circularRangeAndWithoutRandomInf(self):
        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.enableCircularGrid()
        self.automaton.disableRandomVisitingOfCells()

        rr = [17,18,19,0,1,2,3,4,5]
        rc = [27,28,29,0,1,2,3,4,5]

        ranges = self.automaton.getRanges(1,1,4)

        self.assertEquals(rr,ranges[0],"Not same ranges for rows:"+repr(ranges[0]))
        self.assertEquals(rc,ranges[1],"Not same ranges for columns:"+repr(ranges[1]))

    def test_circularRangeAndWithoutRandomSup(self):
        self.automaton.reinit(ROWS,COLUMNS)
        self.automaton.enableCircularGrid()
        self.automaton.disableRandomVisitingOfCells()

        rr = [14,15,16,17,18,19,0,1,2]
        rc = [23,24,25,26,27,28,29,0,1]

        ranges = self.automaton.getRanges(18,27,4)

        self.assertEquals(rr,ranges[0],"Not same ranges for rows:"+repr(ranges[0]))
        self.assertEquals(rc,ranges[1],"Not same ranges for columns:"+repr(ranges[1]))

    def test_rangeWithoutRandomInf(self):
        self.automaton.reinit(ROWS,COLUMNS)

        rr = [0,1,2,3,4,5]
        rc = [0,1,2,3,4,5]

        ranges = self.automaton.getRanges(1,1,4)
        ranges[0].sort()
        ranges[1].sort()

        self.assertEquals(rr,ranges[0],"Not same ranges for rows:"+repr(ranges[0]))
        self.assertEquals(rc,ranges[1],"Not same ranges for columns:"+repr(ranges[1]))

    def test_rangeWithoutRandomSup(self):
        self.automaton.reinit(ROWS,COLUMNS)

        rr = [14,15,16,17,18,19]
        rc = [23,24,25,26,27,28,29]

        ranges = self.automaton.getRanges(18,27,4)
        ranges[0].sort()
        ranges[1].sort()

        self.assertEquals(rr,ranges[0],"Not same ranges for rows:"+repr(ranges[0]))
        self.assertEquals(rc,ranges[1],"Not same ranges for columns:"+repr(ranges[1]))


if __name__ == '__main__':
    unittest.main()

