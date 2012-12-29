import numpy as np 
from Agent import Agent
from Cell import Cell
import random

class Grid(object):
    
    def __init__(self,rows,columns):
        self.agentTrack = []
        self.nextAgentTrack = []
        self.reinit(rows,columns)
        self.convergence = False
        
    def reinit(self,rows,columns):
        self.rows = rows
        self.columns = columns
        
        self.world = np.ndarray(shape=(rows,columns),dtype=Cell)
        self.nextWorld = np.empty(shape=(rows,columns),dtype=Cell)
        self.clear()
         
    def createPopulation(self, number, radius, fitness = None):

        for i in range(number):
            row = np.random.randint(self.rows)
            column = np.random.randint(self.columns)
            self.addAgent(Agent(row,column,radius, fitness))
            
    def clear(self):
        self.agentTrack[:] = []
        for r in range(self.rows):
            for c in range(self.columns):
                self.world[r,c] = Cell(r,c)
                self.nextWorld[r,c] = Cell(r,c)
         
    def addAgent(self, agent):
        loc = agent.location
        self.world[loc.row,loc.column].addAgent(agent)
        self.agentTrack.append(agent)


    def clearNextWorld(self):
        for r in range(self.rows):
            for c in range(self.columns):
                self.nextWorld[r,c] = Cell(r,c)
                
    def getNeighbors(self,*args):
              
        if len(args) == 2:
            row = args[0].row
            column = args[0].column
            radius = args[1]
        else: #len(args) = 3
            row = args[0]
            column = args[1]
            radius = args[2]    
            
        neibohrs = []
        limitRow = [0,self.rows]
        limitColumn = [0,self.columns]

        if radius == -1:
            initialRow = limitRow[0]
            initialColumn = limitRow[0]
            
            finalRow = limitRow[1]
            finalColumn = limitColumn[1]
        else:
            #self.radius = np.random.randint(5)
            initialRow = row - radius
            initialColumn = column - radius

            finalRow = row + radius
            finalColumn = column + radius
         
        rangeRow = random.sample(range(initialRow,finalRow + 1), finalRow - initialRow)
        rangeCol = random.sample(range(initialColumn,finalColumn + 1), finalColumn - initialColumn)

        for r in rangeRow:
            if limitRow[0] <= r < limitRow[1]:
                for c in rangeCol:
                    if  limitColumn[0] <= c < limitColumn[1] and r != row and c != column:
                        neibohrs.append(self.getCell(r,c))
        
        return  neibohrs
        
    def getCell(self,*args):
        if len(args) == 1:
            return self.world[args[0].row,args[0].column] 
        
        if len(args) == 2: 
            return self.world[args[0],args[1]]     
                
    #TODO: REMOVE            
    def getAgents(self,*args):           
        if len(args) == 0:
            return self.agentTrack
        
        if len(args) == 1: 
            return self.world[args[0].row,args[0].column].getAgents()
       
        if len(args) == 2: 
            return self.world[args[0],args[1]].getAgents()    
          
    def step(self):
        self.clearNextWorld()
        self.convergence = True
        
        for agent in self.getAgents():
            loc = agent.location
            agent.step(self)
            nextLoc = agent.nextLocation
                       
            nextLoc = agent.nextLocation
            self.nextWorld[nextLoc.row,nextLoc.column].addAgent(agent)  
        
            if loc.row != nextLoc.row or loc.column != nextLoc.column:
                self.convergence = False

        self.updateGrid()

    def updateGrid(self):      
        for r in range(self.rows):
            for c in range(self.columns):
                self.world[r,c] = self.nextWorld[r,c]
        
        for agent in self.agentTrack:
            agent.updateState()

    def isConvergence(self):                 
        return self.convergence

    def getMatrixOfPopulation(self):
        array = np.zeros((self.rows,self.columns),dtype=int)
        for r in range(self.rows):
            for c in range(self.columns):
                array[r,c] = self.getCell(r,c).countAgents()

        return array


    def __str__(self):
        array = self.getMatrixOfPopulation()
        return repr(array)
    
 