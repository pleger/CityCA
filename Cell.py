"""
The objects of this class are cells of a grid. A cell contains agents and positive and/or negative externalities.
"""

from Location import Location


class Cell(object):
    
    def __init__(self, row, column):
        """TODO: COMMENT METHOD
        """
        self.location = Location(row,column)
        self.agents = []
        self.externalities = []
          
    def addAgent(self,agent):
        """TODO: COMMENT METHOD
        """
        self.agents.append(agent)
  
    def getAgents(self):
        """TODO: COMMENT METHOD
        """
        return self.agents
    
    def countAgents(self):
        """TODO: COMMENT METHOD
        """
        return len(self.agents)

    def __str__(self):
        """TODO: COMMENT METHOD
        """
        return str(self.countAgents())

    def __repr__(self):
        """TODO: COMMENT METHOD
        """
        return self.__str__()
