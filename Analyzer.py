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
        """This method
        """
        if not cls._instance:
            cls._instance = super(Analyzer, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, automaton):
        """This method sets the initial grid
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

        return [y,x]

    def getLinearRegressionData(self, log):
        values = self.createValuesForRegression(log)

        slope, intercept, r_value, p_value, std_err = linregress(values[0], values[1])
        return [slope,intercept,r_value*r_value]

    def createLinearRegressionGraph(self, log, save = False, prefixNameFile = "figure", x = None, y = None):
        #Join with the previous method
        decimal = (10**3)*1.0
        data = self.getLinearRegressionData(log)
        data = [math.trunc(x*decimal)/decimal if not math.isnan(x) else float("nan") for x in data]

        values = self.createValuesForRegression(log)

        now = datetime.datetime.now()
        plt.plot(values[0],values[1],'co')
        plt.xlabel("Ranking")
        plt.ylabel("Population")
        plt.title("Ranking of Population [slope="+str(data[0])+",inter="+str(data[1])+",r2="+str(data[2]) + "]")

        if save:
            plt.savefig(prefixNameFile+".png")
        else:
            plt.show()



    def getRankingOfPopulation(self):
        """This method returns the ranking of population of each cell
        """
        population = []
        for r in range(self.automaton.rows):
            for c in range(self.automaton.columns):
                cell = self.automaton.getCell(r,c)
                if cell.countAgents() > 0:
                    population.append(cell)

        return sorted(population, key = lambda cell: cell.countAgents(), reverse = True)