import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.pylab as pl
import inspect 

#def f():
#    print args.param

#f(velocity = 2)


#from pylab import *
y =[[0.03, 0.86, 0.65, 0.34, 0.34, 0.02, 0.22, 0.74, 0.66, 0.65],
    [0.43, 0.18, 0.63, 0.29, 0.03, 0.24, 0.86, 0.07, 0.58, 0.55],
    [0.66, 0.75, 0.01, 0.94, 0.72, 0.77, 0.20, 0.66, 0.81, 0.52]]

#print len(y[0])
#print len(x)

N = 10
x = 0.9*pl.rand(N)

area = pl.pi*(10 * pl.rand(N))**2 # 0 to 10 point radiuses
fig = pl.figure()
window = fig.add_subplot(111)
sca = window.scatter(x,y[0],s=30,c=area)

def metric():
    return 0.9*pl.rand(N)

def update(data):
    path = sca.get_paths()
    print "BKN"
    #for pro, value in vars(sca).iteritems():
    #    print pro, ": ", value
    
    print [name for name,thing in inspect.getmembers(sca)]
    
    return window.scatter(x,data,s=30,c=area)

#scatter(x,y,s=area, marker='', c='b')
#hexbin(x,y,cmap=cm.hsv) 
#fig.colorbar()


ani = animation.FuncAnimation(fig, update, y, interval=2*1000)


#ani = animation.FuncAnimation(fig, update, data_gen, interval=100)

pl.show()