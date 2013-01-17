import sys
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

    def enableLogScale(self):
        self.log = True

    def run(self):
        """
        Comment for this method
        """

        counter = 0
        for exp in self.exps:
            experiment = exp[1]
            name = exp[0]
            counter +=  1
            arr = []
            self.run = types.MethodType(experiment,self,Benchmarks)

            innerResult = [0,0,0]
            for r in range(self.repeat):
                print ("REPEAT:"+str(r))
                self.run()

                if r == 0: #to generate data
                    arr.append(name)
                    arr.append(repr(self.automaton.rows)+"x"+repr(self.automaton.columns))
                    arr.append(repr(self.automaton.rmin))
                    arr.append(repr(self.automaton.rmax))
                    arr.append(repr(len(self.automaton.getAgents())))

                self.analyzer.createLinearRegressionGraph(self.log, save = True, prefixNameFile = self.directory+
                                                                                                  "/imgs/figure-"+arr.__str__())
                innerResult = [(x + y) for x, y  in zip(innerResult, self.analyzer.getLinearRegressionData(self.log))]

            innerResult = [x/self.repeat for x in innerResult]

            arr.append(repr(self.simulation.iterations))
            arr += innerResult
            self.results.append(arr)

            print "Finished name:"+name+" ("+str(counter)+ "/" + str(len(self.exps))+")"

        self.generateReport()

    def now(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d-%H-%M").__str__()

    def generateReport(self):
        f = open(self.directory+"/report-"+self.now()+".txt",'w')
        text = "Name,Z,rmin,rmax,Ite,agents,slope,intercept"
        f.write(text+"\n")

        for result in self.results:
            text = repr(result[0])+","+repr(result[1])+","+repr(result[2])+","+repr(result[3])+","
            text += repr(result[4])+","+repr(result[5])+","+repr(result[6])+","+repr(result[7])
            f.write(text+"\n")

        f.close()

if __name__ == '__main__':
    POPULATION = 2000
    ITERATION = 4

    automaton = Automaton(1,1) # stupid values
    bench = Benchmarks(automaton)

    def exp1(self):
        self.automaton.reinit(40,40)
        self.automaton.createPopulation(POPULATION, Agent.constRadium(5))
        self.simulation.start(ITERATION)

    def exp2(self):
        self.automaton.reinit(40,40)
        self.automaton.createPopulation(POPULATION, Agent.randomRangeRadiumNormal(5,7))
        self.simulation.start(ITERATION)

    def exp3(self):
        self.automaton.reinit(40,40)
        self.automaton.createPopulation(POPULATION, Agent.randomRangeRadiumUnif(1,8))
        self.simulation.start(ITERATION)

    def exp4(self):
        self.automaton.reinit(50,50)
        rmin = self.automaton.rmin
        rmax = self.automaton.rmax

        self.automaton.createPopulation(POPULATION, Agent.randomRangeRadiumUnif(rmin,rmax))
        self.simulation.start(ITERATION)

    def exp5(self):
        self.automaton.reinit(50,50)
        rmin = self.automaton.rmin
        rmax = self.automaton.rmax

        self.automaton.createPopulation(POPULATION, Agent.randomRangeRadiumNormal(rmin,rmax))
        self.simulation.start(ITERATION)

    bench.addExp(exp1,"constRadium")
    bench.addExp(exp2,"normRadium5-7")
    bench.addExp(exp3,"unifRadium1-8")
    bench.addExp(exp4,"unifRadium-min-max")
    bench.addExp(exp5,"normalRadium-min-max")

    bench.enableLogScale()
    bench.setRepeat(3)
    initialTime = datetime.datetime.now()
    print "BEGIN BENCH"
    bench.run()
    print "END BENCH"
    finalTime = datetime.datetime.now()
    deltaTime = finalTime - initialTime

    fileNameZip = "expResult-"+bench.now()+".zip"
    os.system("zip -r "+fileNameZip+" exps")
    # To work with mail, it is necessary to config sendmail
    os.system("echo 'Available results (Time: "+ deltaTime.__str__() +"): http://pleger.cl/ChileCA/"+fileNameZip+"' | mail -s 'ChileCA Results Available' pleger@gmail.com")





