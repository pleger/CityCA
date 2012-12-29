from Location import Location


class Cell(object):
    
    def __init__(self, row, column):
        self.location = Location(row,column)
        self.agents = []
        self.externs = []
          
    def addAgent(self,agent):
        self.agents.append(agent)
  
    def getAgents(self):
        return self.agents
    
    def countAgents(self):
        return len(self.agents)

    def __eq__(self, other):
        return self.countAgents() - other.countAgents()

    def __str__(self):
        return str(self.countAgents())

    def __repr__(self):
        return self.__str__()
