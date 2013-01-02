"""
The objects of this class are cells of a grid. A cell contains agents and positive and/or negative externalities.
"""

from Location import Location


class Cell(object):
    
    def __init__(self, row, column):
        self.location = Location(row,column)
        self.agents = []
        self.externalities = []
          
    def addAgent(self,agent):
        self.agents.append(agent)
  
    def getAgents(self):
        return self.agents
    
    def countAgents(self):
        return len(self.agents)

    def __str__(self):
        return str(self.countAgents())

    def __repr__(self):
        return self.__str__()
