"""
This class represents agents inside of a cell (and obliviously inside of grid as well)
"""

from Location import Location
import types


class Agent(object):    
     
    def __init__(self,row,column,radius, fitness = None):
        self.location = Location(row,column) #TODO: It doesn't need an agent
        self.radius = radius

        #Change the strategy
        if fitness:
            self.setFitness(fitness)

    def setFitness(self,fitness):
        self.getFitness = types.MethodType(fitness,self,Agent)

    #default behavior
    def getFitness(self,cell, own = False):
        n = cell.countAgents()
        return (n + 1)  if not own else n         
    
    def step(self,grid):
        self.nextLocation = self.getBestLocation(grid)
  
    def getBestLocation(self,grid):
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
        self.location.row = self.nextLocation.row
        self.location.column = self.nextLocation.column
        
    
    def __repr__(self):
        return repr(self.row) + "," + repr(self.column)

    def __repr__(self):
        return self.__str__()