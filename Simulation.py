"""
This class carries out the simulation of the cellular automaton
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Simulation(object):
    
    SIZE_BALLS = 100
    INTERVAL = 1
    DEBUG_ITERATIONS = -1
    
    def __init__(self,automaton, iterations, animation):
        """TODO: COMMENT METHOD        """
        self.iterations = iterations
        self.automaton = automaton
        self.fig, self.ax = plt.subplots(figsize=(15, 5))

        plt.title("Simulation of New Net Logo")
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")
    
        self.animation = animation

    def start(self):
        """TODO: COMMENT METHOD
        """
        if self.animation:
            ani = animation.FuncAnimation(self.fig, self.__animate, init_func=self.__setupPlot, interval = Simulation.INTERVAL,
                frames = self.iterations, repeat = False, save_count = 2)

            plt.show()

        else:
            for i in range(self.iterations):
                self.automaton.step()
                self.__showConsoleInf(i)

    def __showConsoleInf(self,i):
        """TODO: COMMENT METHOD
        """
        text = ""
        if i % Simulation.DEBUG_ITERATIONS == 0 and Simulation.DEBUG_ITERATIONS != -1:
            text += "iter:" + repr(i) + " "
            text += "conv:" + repr(self.automaton.convergence) + " "
            print text

        if i == self.iterations - 1:
            print "END"

    def __setupPlot(self):
        """TODO: COMMENT METHOD
        """
        points,colors = self.__convertToGraph(True)
        population = len(self.automaton.getAgents())

        self.scat = self.ax.scatter(points[0], points[1], c = colors, s = Simulation.SIZE_BALLS, vmin = 0, vmax = population)
        self.ax.axis([0, self.automaton.columns - 1, 0, self.automaton.rows - 1])
       
        plt.colorbar(self.scat)

            
    def __animate(self,i):
        """TODO: COMMENT METHOD
        """
        self.automaton.step()
        self.__showConsoleInf(i)
    
        points,colors = self.__convertToGraph()
        self.scat.set_offsets(points)
        self.scat.set_array(colors)
        return self.scat,    
    
        
    def __convertToGraph(self, setup = False):
        """TODO: COMMENT METHOD
        """
        agents = self.automaton.getAgents()
        points = []
        colors = []
        
        for agent in agents:
            loc = agent.location
            y = loc.row
            x = loc.column
            points.append([x,y])    
            colors.append(self.automaton.getCell(y,x).countAgents())
        
        if not setup:
            return points, np.asanyarray(colors)
        else:
            return self.__splitPoints(points), np.asanyarray(colors)
        
        
    def __splitPoints(self,points):
        """TODO: COMMENT METHOD
        """
        x = []
        y = []    
        for point in points:
            y.append(point[0])
            x.append(point[1])        
        
        return x,y
        
        
        