"""
This class represents agents inside of a cell (and obliviously inside of grid as well)
"""

from Location import Location
from numpy import random
import types


class Agent(object):    
    #TODO: FITNESS FUNCTIONS AS LIBRARY
    def __init__(self,row,column,radius, fitness = None):
        """TODO: COMMENT METHOD
        """
        self.location = Location(row,column) #TODO: It doesn't need an agent
        self.radius = radius

        #Sets fitness functions
        if fitness:
            self.setFitness(fitness)
        else:
            self.setFitness(Agent.defaultFitness)

    def setFitness(self,fitness):
        """This method sets the default fitness behavior
         """
        self.getFitness = types.MethodType(fitness,self,Agent)

    def step(self,grid):
        """TODO: COMMENT METHOD
        """
        self.nextLocation = self.getBestLocation(grid)
  
    def getBestLocation(self,grid):
        """TODO: COMMENT METHOD
        """
        maxLoc = self.location
        maxFitness = self.getFitness(grid.getCell(maxLoc), own = True)
        cells = grid.getNeighbors(maxLoc,self.radius)
        
        for cell in cells:
            fitness = self.getFitness(cell) #change this value
            
            if maxFitness < fitness:
                maxFitness = fitness
                maxLoc = cell.location
        
        return maxLoc
    
    def updateState(self):
        """TODO: COMMENT METHOD
        """
        self.location.row = self.nextLocation.row
        self.location.column = self.nextLocation.column

    def __repr__(self):
        """TODO: COMMENT METHOD
        """
        return repr(self.row) + "," + repr(self.column)

    def __repr__(self):
        """TODO: COMMENT METHOD
        """
        return self.__str__()

    @staticmethod
    def defaultFitness(self, cell, own = False):
        """This method
        """
        n = cell.countAgents()
        n = (n + 1)  if not own else n
        return n

    @staticmethod
    def randomFitness(self,cell, own = False):
        return random.randint(30)