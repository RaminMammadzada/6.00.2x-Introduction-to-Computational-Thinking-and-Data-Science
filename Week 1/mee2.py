import pylab
pylab.figure(1) # make figure 1 current figure
pylab.plot([1,2,3,4],[1,2,3,4]) # draw on figure 1
pylab.figure(2) # make figure 2 current figure
pylab.plot([1,4,2,3],[5,6,7,8]) # draw on figure 2
pylab.savefig("Figure-Eric.png") # save figure 2
pylab.figure(1) # go back to working on figure 1
pylab.plot([5,6,10,3]) # draw again on figure 1
pylab.savefig("Figure-Grimson.png") # save figure 1
