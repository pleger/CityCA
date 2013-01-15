"""
This (singleton) class is used to analyze grid. Concretely, the object of this class allows developers to get results
like the ranking of population
"""

import math
from scipy.stats.stats import linregress
import matplotlib.pyplot as plt
import datetime


class Analyzer(object):
    _instance = None  #only instance of this class

    def __new__(cls, *args, **kwargs):
        """TODO: COMMENT METHOD
        """
        if not cls._instance:
            cls._instance = super(Analyzer, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, automaton):
        """TODO: COMMENT METHOD
        """
        self.automaton = automaton

    def applyLog(self,values):
        return map(math.log10, values)

    def createValuesForRegression(self, log):
        ranking = self.getRankingOfPopulation()
        x = []
        y = []
        c = 1
        for cell in ranking:
            x.append(c)
            y.append(cell.countAgents())
            c += 1

        if log:
            x = self.applyLog(x)
            y = self.applyLog(y)

        return [x,y]

    def getLinearRegressionData(self, log):
        values = self.createValuesForRegression(log)

        slope, intercept, r_value, p_value, std_err = linregress(values[0], values[1])
        return [slope,intercept,r_value*r_value]

    def createLinearRegressionGraph(self, log ,save = False, prefixNameFile = "figure", x = None, y = None):
        #Join with the previous method
        decimal = (10**3)*1.0
        data = self.getLinearRegressionData(False)
        data = [math.trunc(x*decimal)/decimal for x in data]

        if not x or not y:
            values = self.createValuesForRegression(log)
        else:
            values = [x,y]


        now = datetime.datetime.now()
        plt.plot(values[0],values[1],'co')
        plt.xlabel("Ranking")
        plt.ylabel("Population")
        plt.title("Ranking of Population [slope="+str(data[0])+",inter="+str(data[1])+",r2="+str(data[2]) + "]")

        if save:
            plt.savefig("imgs/"+prefixNameFile+"-"+now.__str__()+".png")
        else:
            plt.show()



    def getRankingOfPopulation(self):
        """TODO: COMMENT METHOD
        """
        population = []
        for r in range(self.automaton.rows):
            for c in range(self.automaton.columns):
                cell = self.automaton.getCell(r,c)
                if cell.countAgents() > 0:
                    population.append(cell)

        return sorted(population, key = lambda cell: cell.countAgents(), reverse = True)