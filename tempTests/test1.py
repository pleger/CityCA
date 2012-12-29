from numpy import *
from Cell import Cell

rows = 2
columns = 3

def t():
    t1 = [2,2,5]
    t2 = [5,6,7]
    
    return t1,t2

x1,x2 = t()

#print repr(x1) + " " + repr(x2)



world = ndarray(shape=(rows,columns),dtype=Cell)
world[0,0] = Cell(3,4)

world[0,0].addAgents(3)

print world

#offsets = random.rand(20,2)

#print offsets