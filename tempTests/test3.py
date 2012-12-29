import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def main():
    numframes = 2
    numpoints = 3
    positions = np.random.random((numframes,numpoints,2))

    
    color_data = np.random.random((numframes, numpoints))
    #print len(color_data)
    x, y, c = np.random.random((3, numpoints))

    fig = plt.figure()
    scat = plt.scatter(x, y, c=c, s=100)
    plt.colorbar()
    
    #tt = scat.get_offsets()
    #print tt
    
    #print np.random.random((4,3,2))

    ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes),
                                 fargs=(positions, scat))
    plt.show()

    #a = np.ndarray(shape=(2,2), dtype=int)
    #a = np.arange(15).reshape(3,5)
    #print type(a)
    #a[0,0] = -2
    #a[1,1] = 5
    #print a

def update_plot(i, data, scat):
    print "DATA %s" % data
    scat.set_offsets(data)
    #scat.set_array(data1[i])
    return scat,

main()