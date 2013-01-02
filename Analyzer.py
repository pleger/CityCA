"""
This (singleton) class is used to analyze grid. Concretely, the object of this class allows developers to get results
like the ranking of population
"""


class Analyzer(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Analyzer, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, grid):
        self.grid = grid


    def getRankingOfPopulation(self):
        population = []
        count = len(self.grid.getAgents())
        for r in range(self.grid.rows):
            for c in range(self.grid.columns):
                cell = self.grid.getCell(r,c)
                if cell.countAgents() > 0:
                    population.append(cell)

        return sorted(population, key = lambda cell: cell.countAgents(), reverse = True)