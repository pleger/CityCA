"""
This (singleton) class is used to analyze grid. Concretely, the object of this class allows developers to get results
like the ranking of population
"""

from scipy.stats.stats import linregress


class Analyzer(object):
    _instance = None  #only instance of this class

    def __new__(cls, *args, **kwargs):
        """TODO: COMMENT METHOD
        """
        if not cls._instance:
            cls._instance = super(Analyzer, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, grid):
        """TODO: COMMENT METHOD
        """
        self.grid = grid

    def getLinearRegressionData(self):
        ranking = self.getRankingOfPopulation()
        x = []
        y = []
        c = 1
        for cell in ranking:
            x.append(c)
            y.append(cell.countAgents())
            c += 1

        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        return [slope,intercept,r_value*r_value]



    def getRankingOfPopulation(self):
        """TODO: COMMENT METHOD
        """
        population = []
        for r in range(self.grid.rows):
            for c in range(self.grid.columns):
                cell = self.grid.getCell(r,c)
                if cell.countAgents() > 0:
                    population.append(cell)

        return sorted(population, key = lambda cell: cell.countAgents(), reverse = True)