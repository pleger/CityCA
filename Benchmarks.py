from Automaton import Automaton
from Simulation import Simulation
from Analyzer import Analyzer
from Agent import Agent
#from __future__ import print
import datetime
import types


class Benchmarks(object):

    def __init__(self, automaton):
        self.exps = []
        self.automaton = automaton
        self.simulation = Simulation(automaton, False)
        self.analyzer = Analyzer(automaton)
        self.results = []
        self.repeat = 1
        self.simulation.DEBUG_ITERATIONS = 5

    def addExp(self,exp):
        self.exps.append(exp)

    def setRepeat(self,repeat):
        self.repeat = repeat

    def run(self):

        for exp in self.exps:
            arr = []
            self.run = types.MethodType(exp,self,Benchmarks)
            arr.append(repr(self.automaton.rows)+"x"+repr(self.automaton.columns))
            arr.append(repr(self.automaton.rmin))
            arr.append(repr(self.automaton.rmax))


            result = [0,0,0]
            for r in range(self.repeat):
                self.run()
                result = [(x + y) for x, y  in zip(result, self.analyzer.getLinearRegressionData(False))]
            result = [x/3 for x in result]

            arr.append(repr(self.simulation.iterations))
            arr += result
            self.results.append(arr)

        self.generateReport()

    def generateReport(self):
        now = datetime.datetime.now()
        f = open("report-"+now.__str__()+".csv",'w')
        text = "Z\trmin\trmax\tIte\tb\tconst"
        f.write(text+"\n")

        for result in self.results:
            text = repr(result[0])+"\t"+repr(result[1])+"\t"+repr(result[2])+"\t"+repr(result[3])+"\t"
            text += repr(result[4])+"\t"+repr(result[5])
            f.write(text+"\n")

        f.close()

if __name__ == '__main__':
    automaton = Automaton(1,1) # stupid values
    bench = Benchmarks(automaton)

    def exp1(self):
        self.automaton.reinit(40,20)
        self.automaton.createPopulation(30, Agent.maxRadium(5))
        self.simulation.start(20)

    def exp2(self):
        self.automaton.reinit(40,20)
        self.automaton.createPopulation(30, Agent.randomRangeRadiumNormal(5,7))
        self.simulation.start(20)

    def exp3(self):
        self.automaton.reinit(40,20)
        self.automaton.createPopulation(30, Agent.randomRangeRadiumUnif(1,8))
        self.simulation.start(10)

    def exp4(self):
        self.automaton.reinit(50,50)
        rmin = self.automaton.rmin
        rmax = self.automaton.rmax

        self.automaton.createPopulation(12, Agent.randomRangeRadiumUnif(rmin,rmax))
        self.simulation.start(30)


    bench.addExp(exp1)
    bench.addExp(exp2)
    bench.addExp(exp3)
    bench.addExp(exp4)

    bench.setRepeat(3)
    print "BEGIN BENCH"
    bench.run()
    print "END BENCH"






