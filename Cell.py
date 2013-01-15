"""
The objects of this class are cells of a grid. A cell contains agents and positive and/or negative externalities.
"""

from Location import Location


class Cell(object):
    
    def __init__(self, row, column):
        """This method sets the location, agents and externalities of a cell
        """
        self.location = Location(row,column)
        self.agents = []
        self.externalities = []
          
    def addAgent(self,agent):
        """This method adds agents
        """
        self.agents.append(agent)
  
    def getAgents(self):
        """This method gets
        """
        return self.agents
    
    def countAgents(self):
        """This method counts the agents from a cell
        """
        return len(self.agents)

    def __str__(self):
        """This method returns the string of the numbers of agents
        """
        return str(self.countAgents())

    def __repr__(self):
        """TODO: COMMENT METHOD
        """
        return self.__str__()
