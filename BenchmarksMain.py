
"""
 def exp1(self):
     self.automaton.reinit(50,50)
     self.automaton.createPopulation(POPULATION, Agent.constRadium(RMAX))
     self.simulation.start(ITERATION)

 def exp2(self):
     self.automaton.reinit(50,50)
     self.automaton.createPopulation(POPULATION, Agent.randomRangeRadiumNormal(RMIN,RMAX))
     self.simulation.start(ITERATION)

 def exp3(self):
     self.automaton.reinit(50,50)
     self.automaton.createPopulation(POPULATION, Agent.randomRangeRadiumUnif(RMIN,RMAX))
     self.simulation.start(ITERATION)

  bench.addExp(exp1,"constRadium-15")
    bench.addExp(exp2,"normRadium1-15")
    bench.addExp(exp3,"unifRadium1-15")
 """

from Benchmarks import Benchmarks
from Automaton import Automaton
from Agent import Agent
import datetime
import os



__author__ = 'pleger'

if __name__ == '__main__':
    POPULATION = 12000
    ITERATION = 50
    RMIN = 1
    RMAX = 15
    SIZE_Y = 10
    SIZE_X = 50

    bench = Benchmarks(Automaton(1,1))

    def expsPapers():
        exps = []

        for rmax in [RMAX]:

            def exp(self):

                self.automaton.reinit(SIZE_X, SIZE_Y)
                self.simulation.enableConvergenceStop()

                self.automaton.disableRandomVisitingOfCells()
                #self.automaton.enableCircularGrid()

                self.automaton.createPopulation(POPULATION, Agent.randomRangeRadiumUnif(RMIN,rmax))
                self.simulation.start(ITERATION)

            exps.append(["normal-1-"+str(rmax),exp])

        #for rmax in [1,5,10,15,25]:
        #    def exp(self):
        #        self.automaton.reinit(50,50)
        #        self.automaton.createPopulation(POPULATION, Agent.randomRangeRadiumNormal(1,rmax), Agent.deagglomerationForceFitness)
        #        self.simulation.start(ITERATION)
        #
        #    exps.append(["degla-normal-1-"+str(rmax),exp])

        return exps

    bench.addExps(expsPapers())

    bench.enableLogScale()
    bench.setRepeat(2)

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

