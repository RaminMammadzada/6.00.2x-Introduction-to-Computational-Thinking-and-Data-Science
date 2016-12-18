import pylab
import simWalkts from mee4.py

def drunkTestP(numTrials = 50):
    stepsTaken=[10,100,1000,10000]
    meanDistances=[]
    for numSteps in stepsTaken:
        distances=simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTken, meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()
