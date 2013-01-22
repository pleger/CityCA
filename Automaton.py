"""
This class represents the grid of the cellular automaton.
"""


from numpy import zeros, random, empty, ndarray
from Agent import Agent
from Cell import Cell
import random as rn
import math
import sys



class Automaton(object):
    
    def __init__(self, rows, columns):
        """This method resets the rows and columns of the grid
        """
        self.reinit(rows, columns)
        
    def reinit(self,rows,columns):
        """This method sets the rows and columns as default
        """
        self.cached = True
        self.cacheFitness = ndarray(shape=(rows,columns),dtype=float)
        self.rows = rows
        self.columns = columns
        self.rmin = 1
        self.rmax = max(rows,columns)

        self.agentTrack = []
        self.nextAgentTrack = []


        self.cellGrid = ndarray(shape=(rows,columns),dtype=Cell)
        self.nextCellGrid = empty(shape=(rows,columns),dtype=Cell)
        self.__clear()

    def disableCache(self):
        self.cached = False

    def setCachedValue(self, cell, value):
        self.cacheFitness[cell.location.row, cell.location.column] = value

    def getHasCachedValue(self, cell):
        return not self.cacheFitness[cell.location.row, cell.location.column] == sys.float_info.min and self.cached == True

    def getCachedValue(self, cell):
        return self.cacheFitness[cell.location.row, cell.location.column]

    def createPopulation(self, number, radius, fitness = None):
        """This method creates the agents and put them in the grid
        """
        for i in range(number):
            row = random.randint(self.rows)
            column = random.randint(self.columns)
            self.addAgent(Agent(row,column,radius, fitness))

         
    def addAgent(self, agent):
        """This method adds a location to the agents
        """
        loc = agent.location
        self.cellGrid[loc.row,loc.column].addAgent(agent)
        self.agentTrack.append(agent)

                
    def getNeighbors(self,*args):
        """This method gets the numbers of the neighbors (It depends of the radius)
        """
        #TODO: IMPROVE IFs
        if len(args) == 2:
            row = args[0].row
            column = args[0].column
            radius = args[1]
        else: #len(args) = 3
            row = args[0]
            column = args[1]
            radius = args[2]    
            
        neighbors = []
        limitRow = [0,self.rows]
        limitColumn = [0,self.columns]

        #todo improve this code
        if radius == -1:
            initialRow = limitRow[0]
            initialColumn = limitRow[0]
            
            finalRow = limitRow[1] - 1
            finalColumn = limitColumn[1] - 1
        else:
            initialRow = row - radius
            initialColumn = column - radius

            finalRow = row + radius
            finalColumn = column + radius

            initialRow = limitRow[0] if initialRow < limitRow[0] else initialRow
            initialColumn = limitColumn[0] if initialColumn < limitColumn[0] else initialColumn

            finalRow = limitRow[1] - 1 if finalRow >= limitRow[1] else finalRow
            finalColumn = limitColumn[1] - 1 if finalColumn >= limitColumn[1] else finalColumn

        rangeRow = rn.sample(range(initialRow,finalRow + 1), finalRow - initialRow + 1)
        rangeCol = rn.sample(range(initialColumn,finalColumn + 1), finalColumn - initialColumn + 1)

        for r in rangeRow:
                for c in rangeCol:
                    if  r != row and c != column:
                        neighbors.append(self.getCell(r,c))
        
        return  neighbors
        
    def getCell(self,*args):
        """This method
        """
        if len(args) == 1:
            return self.cellGrid[args[0].row,args[0].column]
        
        if len(args) == 2: 
            return self.cellGrid[args[0],args[1]]
                
    #TODO: REMOVE            
    def getAgents(self,*args):
        """This method gets the
        """
        if len(args) == 0:
            return self.agentTrack
        
        if len(args) == 1: 
            return self.cellGrid[args[0].row,args[0].column].getAgents()
       
        if len(args) == 2: 
            return self.cellGrid[args[0],args[1]].getAgents()
          
    def step(self):
        """This method updates the grid to the next step
        """
        self.__clearNextWorld()
        self.convergence = True
        
        for agent in self.getAgents():
            loc = agent.location
            agent.step(self)
            nextLoc = agent.nextLocation
                       
            nextLoc = agent.nextLocation
            self.nextCellGrid[nextLoc.row,nextLoc.column].addAgent(agent)
        
            if loc.row != nextLoc.row or loc.column != nextLoc.column:
                self.convergence = False

        self.__updateGrid()


    def getMatrixOfPopulation(self):
        """This method gets the array of population of the grid
        """
        array = zeros((self.rows,self.columns),dtype=int)
        for r in range(self.rows):
            for c in range(self.columns):
                array[r,c] = self.getCell(r,c).countAgents()

        return array

    def __updateGrid(self):
        """This method
        """
        for r in range(self.rows):
            for c in range(self.columns):
                self.cellGrid[r,c] = self.nextCellGrid[r,c]

        for agent in self.agentTrack:
            agent.updateState()

    def __clearNextWorld(self):
        """This method clears the next grid state.
        """
        for r in range(self.rows):
            for c in range(self.columns):
                self.nextCellGrid[r,c] = Cell(r,c)
                self.cacheFitness[r,c] = sys.float_info.min

    def __clear(self):
        """This method
        """
        self.convergence = False
        self.agentTrack[:] = []
        for r in range(self.rows):
            for c in range(self.columns):
                self.cellGrid[r,c] = Cell(r,c)
                self.nextCellGrid[r,c] = Cell(r,c)


    def __str__(self):
        """This method
        """
        array = self.getMatrixOfPopulation()
        return repr(array)

    def __repr__(self):
        """This method
        """
        return self.__str__()