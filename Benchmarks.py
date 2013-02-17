import sys
import socket
import matplotlib
if socket.gethostname() == "duck": # To work in "duck" server
    matplotlib.use("Agg")

from Automaton import Automaton
from Simulation import Simulation
from Analyzer import Analyzer
from Agent import Agent
import datetime
import types



class Benchmarks(object):

    def __init__(self, automaton):
        self.exps = []
        self.automaton = automaton
        self.simulation = Simulation(automaton, False)
        self.analyzer = Analyzer(automaton)
        self.repeat = 1.0
        self.simulation.DEBUG_ITERATIONS = -1
        self.directory = "exps"
        self.log = False

    def addExp(self,exp, name):
        self.exps.append([name,exp])

    def addExps(self,exps):
        self.exps += exps

    def setRepeat(self,repeat):
        self.repeat = repeat

    def enableLogScale(self):
        self.log = True

    def run(self):
        """
        Comment for this method
        """
        results = []

        counter = 0
        for exp in self.exps:
            experiment = exp[1]
            name = exp[0]
            counter += 1
            arr = []
            self.run = types.MethodType(experiment,self,Benchmarks)

            innerResult = [0,0,0]
            for r in range(self.repeat):
                self.run()

                if r == 0: #to generate data
                    arr.append(name)
                    arr.append(repr(self.automaton.rows)+"x"+repr(self.automaton.columns))
                    arr.append(repr(self.automaton.rmin))
                    arr.append(repr(self.automaton.rmax))
                    arr.append(repr(len(self.automaton.getAgents())))

                self.analyzer.createLinearRegressionGraph(self.log, save = True, prefixNameFile = self.directory+
                                                                                                  "/imgs/figure-"+arr.__str__()+"-repeat-"+str(r))
                innerResult = [(x + y) for x, y  in zip(innerResult, self.analyzer.getLinearRegressionData(self.log)+
                                                                     [repr(self.simulation.iterations)])]

            innerResult = [x/self.repeat for x in innerResult]

            arr += innerResult
            results.append(arr)

            print "Finished name:"+name+" ("+str(counter)+ "/" + str(len(self.exps))+")"

        self.generateReport(results)

    def now(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d-%H-%M").__str__()

    def generateReport(self, results):
        f = open(self.directory+"/report-"+self.now()+".txt",'w')
        text = "Name;Z;rmin;rmax;agents;slope;intercept;r2;inter"
        f.write(text+"\n")

        for result in results:
            text = repr(result[0])+";"+repr(result[1])+";"+repr(result[2])+";"+repr(result[3])+";"
            text += repr(result[4])+";"+repr(result[5])+";"+repr(result[6])+";"+repr(result[7])+";"+repr(result[8])
            f.write(text+"\n")

        f.close()






