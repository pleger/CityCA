import socket
import matplotlib
if socket.gethostname() == "duck": # To work in "duck" server
    matplotlib.use("Agg")

import os
from Automaton import Automaton
from Simulation import Simulation
from Analyzer import Analyzer
from Agent import Agent
import datetime
import types
import os


class Benchmarks(object):

    def __init__(self, automaton):
        self.exps = []
        self.automaton = automaton
        self.simulation = Simulation(automaton, False)
        self.analyzer = Analyzer(automaton)
        self.results = []
        self.repeat = 1.0
        self.simulation.DEBUG_ITERATIONS = -1
        self.directory = "exps"
        self.log = False

    def addExp(self,exp, name):
        self.exps.append([name,exp])

    def setRepeat(self,repeat):
        self.repeat = repeat

    def setScaleLog(self, log):
        self.log = log

    def run(self):

        """
        Comment for this method
        """
        #Change directory temporally
        os.chdir(self.directory)

        counter = 0
        for exp in self.exps:
            experiment = exp[1]
            name = exp[0]
            counter +=  1
            arr = []
            self.run = types.MethodType(experiment,self,Benchmarks)

            result = [0,0,0]
            for r in range(self.repeat):
                self.run()

                if r == 1: #to generate data
                    arr.append(repr(self.automaton.rows)+"x"+repr(self.automaton.columns))
                    arr.append(repr(self.automaton.rmin))
                    arr.append(repr(self.automaton.rmax))

                self.analyzer.createLinearRegressionGraph(self.log, save = True, prefixNameFile = "figure-"+name+"-"+arr.__str__())
                result = [(x + y) for x, y  in zip(result, self.analyzer.getLinearRegressionData(self.log))]

            result = [x/self.repeat for x in result]

            arr.append(repr(self.simulation.iterations))
            arr += result
            self.results.append(arr)

            print "Finished name:"+name+" ("+str(counter)+ "/" + str(len(self.exps))+")"


        self.generateReport()

    def generateReport(self):
        now = datetime.datetime.now()
        f = open("report-"+now.__str__()+".csv",'w')
        text = "Z\trmin\trmax\tIte\tslope\tintercept"
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
        self.automaton.reinit(40,40)
        self.automaton.createPopulation(12000, Agent.constRadium(5))
        self.simulation.start(30)

    def exp2(self):
        self.automaton.reinit(40,40)
        self.automaton.createPopulation(12000, Agent.randomRangeRadiumNormal(5,7))
        self.simulation.start(30)

    def exp3(self):
        self.automaton.reinit(40,40)
        self.automaton.createPopulation(12000, Agent.randomRangeRadiumUnif(1,8))
        self.simulation.start(30)

    def exp4(self):
        self.automaton.reinit(50,50)
        rmin = self.automaton.rmin
        rmax = self.automaton.rmax

        self.automaton.createPopulation(12000, Agent.randomRangeRadiumUnif(rmin,rmax))
        self.simulation.start(30)

    def exp5(self):
        self.automaton.reinit(50,50)
        rmin = self.automaton.rmin
        rmax = self.automaton.rmax

        self.automaton.createPopulation(12000, Agent.randomRangeRadiumNormal(rmin,rmax))
        self.simulation.start(30)

    bench.addExp(exp1,"constRadium")
    bench.addExp(exp2,"normRadium5-7")
    bench.addExp(exp3,"unifRadium1,8")
    bench.addExp(exp4,"unifRadium-min-max")
    bench.addExp(exp5,"normalRadium-min-max")

    bench.setScaleLog(True)
    bench.setRepeat(1)
    print "BEGIN BENCH"
    bench.run()
    print "END BENCH"

    # To work with mail, it is necessary to config sendmail
    os.system("echo 'Available results :D' | mail -s 'ChileCA Available' pleger@gmail.com")





