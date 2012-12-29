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