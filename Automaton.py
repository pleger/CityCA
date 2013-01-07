"""
This class represents the grid of the cellular automaton.
"""


from numpy import zeros, random, empty, ndarray
from Agent import Agent
from Cell import Cell
import random as rn
import math



class Automaton(object):
    
    def __init__(self, rows, columns):
        """TODO: COMMENT METHOD
        """
        self.reinit(rows, columns)
        
    def reinit(self,rows,columns):
        """TODO: COMMENT METHOD
        """
        self.rows = rows
        self.columns = columns
        self.rmin = 1
        self.rmax = max(rows,columns)

        self.agentTrack = []
        self.nextAgentTrack = []



        self.cellGrid = ndarray(shape=(rows,columns),dtype=Cell)
        self.nextCellGrid = empty(shape=(rows,columns),dtype=Cell)
        self.__clear()
         
    def createPopulation(self, number, radius, fitness = None):
        """TODO: COMMENT METHOD
        """
        for i in range(number):
            row = random.randint(self.rows)
            column = random.randint(self.columns)
            self.addAgent(Agent(row,column,radius, fitness))

         
    def addAgent(self, agent):
        """TODO: COMMENT METHOD
        """
        loc = agent.location
        self.cellGrid[loc.row,loc.column].addAgent(agent)
        self.agentTrack.append(agent)

                
    def getNeighbors(self,*args):
        """TODO: COMMENT METHOD
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

        if radius == -1:
            initialRow = limitRow[0]
            initialColumn = limitRow[0]
            
            finalRow = limitRow[1]
            finalColumn = limitColumn[1]
        else:
            initialRow = row - radius
            initialColumn = column - radius

            finalRow = row + radius
            finalColumn = column + radius
         
        rangeRow = rn.sample(range(initialRow,finalRow + 1), finalRow - initialRow)
        rangeCol = rn.sample(range(initialColumn,finalColumn + 1), finalColumn - initialColumn)

        for r in rangeRow:
            if limitRow[0] <= r < limitRow[1]:
                for c in rangeCol:
                    if  limitColumn[0] <= c < limitColumn[1] and r != row and c != column:
                        neighbors.append(self.getCell(r,c))
        
        return  neighbors
        
    def getCell(self,*args):
        """TODO: COMMENT METHOD
        """
        if len(args) == 1:
            return self.cellGrid[args[0].row,args[0].column]
        
        if len(args) == 2: 
            return self.cellGrid[args[0],args[1]]
                
    #TODO: REMOVE            
    def getAgents(self,*args):
        """TODO: COMMENT METHOD
        """
        if len(args) == 0:
            return self.agentTrack
        
        if len(args) == 1: 
            return self.cellGrid[args[0].row,args[0].column].getAgents()
       
        if len(args) == 2: 
            return self.cellGrid[args[0],args[1]].getAgents()
          
    def step(self):
        """TODO: COMMENT METHOD
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
        """TODO: COMMENT METHOD
        """
        array = zeros((self.rows,self.columns),dtype=int)
        for r in range(self.rows):
            for c in range(self.columns):
                array[r,c] = self.getCell(r,c).countAgents()

        return array

    def __updateGrid(self):
        """TODO: COMMENT METHOD
        """
        for r in range(self.rows):
            for c in range(self.columns):
                self.cellGrid[r,c] = self.nextCellGrid[r,c]

        for agent in self.agentTrack:
            agent.updateState()

    def __clearNextWorld(self):
        """TODO: COMMENT METHOD
        """
        for r in range(self.rows):
            for c in range(self.columns):
                self.nextCellGrid[r,c] = Cell(r,c)

    def __clear(self):
        """TODO: COMMENT METHOD
        """
        self.convergence = False
        self.agentTrack[:] = []
        for r in range(self.rows):
            for c in range(self.columns):
                self.cellGrid[r,c] = Cell(r,c)
                self.nextCellGrid[r,c] = Cell(r,c)


    def __str__(self):
        """TODO: COMMENT METHOD
        """
        array = self.getMatrixOfPopulation()
        return repr(array)

    def __repr__(self):
        """TODO: COMMENT METHOD
        """
        return self.__str__()