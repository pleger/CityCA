"""
This class represents agents inside of a cell (and obliviously inside of grid as well)
"""

from Location import Location
from numpy import random
import types


class Agent(object):    
    #TODO: FITNESS FUNCTIONS AS LIBRARY
    def __init__(self,row,column,radius, fitness = None):
        """This method sets the initial agents
        """
        self.location = Location(row,column) #TODO: It doesn't need an agent
        self.radius = radius()

        #Sets fitness functions
        if fitness:
            self.setFitness(fitness)
        else:
            self.setFitness(Agent.defaultFitness)

    def setFitness(self,fitness):
        """This method sets the default fitness behavior
         """
        self.getFitness = types.MethodType(fitness,self,Agent)

    def step(self,automaton):
        """This method sets the next location of the agent as the best location
        """
        self.nextLocation = self.getBestLocation(automaton)
  
    def getBestLocation(self,automaton):
        """This method finds the best location to move the agent by using the fitness function
        """
        maxLoc = self.location
        maxFitness = self.getFitness(automaton.getCell(maxLoc), own = True)
        cells = automaton.getNeighbors(maxLoc,self.radius)
        
        for cell in cells:

            if automaton.getHasCachedValue(cell):
                fitness = automaton.getCachedValue(cell)
            else:
                fitness = self.getFitness(cell) #change this value
                automaton.setCachedValue(cell,fitness)

            if fitness < 0:
                print fitness

            if maxFitness < fitness:
                maxFitness = fitness
                maxLoc = cell.location
        
        return maxLoc
    
    def updateState(self):
        """This method updates the location of the agent
        """
        self.location.row = self.nextLocation.row
        self.location.column = self.nextLocation.column

    def __repr__(self):
        """This method returns the present location of the agent
        """
        return repr(self.location.row) + "," + repr(self.location.column)

    def __repr__(self):
        """This method returns...
        """
        return self.__str__()

    @staticmethod
    def defaultFitness(self, cell, own = False):
        """This method returns the numbers of agents of a cell
        """
        n = cell.countAgents()
        n = (n + 1)  if not own else n
        return n

    def paperFitness(self, cell, own = False):
        """This method returns the numbers of agents of a cell
        """
        n = cell.countAgents()
        n = (n + 1)  if not own else n
        return n


    @staticmethod
    def randomFitness(self,cell, own = False):
        return random.randint(30)

    @staticmethod
    def deagglomerationForceFitness(self,cell, own = False):
        c = 0.325
        n = cell.countAgents()
        return n - c*n*n

    #Higher-function for radium
    @staticmethod
    def infiniteRadium():
        def radium():
            return -1
        return radium

    @staticmethod
    def constRadium(r):
        def radium():
            return r
        return radium

    @staticmethod
    def randomRangeRadiumUnif(rmin,rmax):
        def radium():
            return random.randint(rmin,rmax)
        return radium

    @staticmethod
    def randomRangeRadiumBeta(rmin,rmax):
        def radium():
            alpha = 0.5
            beta = 0.2
            return int(random.beta(alpha,beta)*(rmax - rmin) + rmin)
        return radium

    @staticmethod
    def randomRangeRadiumNormal(rmin,rmax):
        def radium():
            value = int(random.normal((rmax+rmin)/2))
            value = rmin if value < rmin else value
            value = rmax if value > rmax else value
            return value
        return radium
