class Location(object):
    def __init__(self,x,y):
        """x nad y are floats"""
        self.x=x
        self.y=y

    def move(self,deltaX, deltaY):
        """deltaX and deltaT are floats"""
        return Location(self.x+deltaX, self.y+deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox=other.x
        oy=other.y
        xDist=self.x-ox
        yDist=self.y-oy
        return (xDist**2+yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

    
class Field(object):
    def __init__(self):
        self.drunk={}

    def addDrunk(self,drunk,loc):
        if drunk in self.drunk:
            raise ValueError('Duplicate drunk')
        else:
            self.drunk[drunk]=loc

    def moveDrunk(self,drunk):
        if not drunk in self.drunk:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation=self.drunk[drunk]
        #use move method of Location to get new location
        self.drunk[drunk] = currentLocation.move(xDist,yDist)

    def getLoc(self,drunk):
        if not drunk in self.drunk:
            raise ValueError('Drunk not in field')
        return self.drunk[drunk]


import random
    
class Drunk(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'This drunk is named' + self.name


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0.0,0.95),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)
    
class EDrunk(Drunk):
    def takeStep(self):
        deltaX=random.random()
        if random.random()<0.5:
            deltaX=-deltaX
        deltaY=random.random()
        if random.random()<0.5:
            deltaY=-deltaY
        return(deltaX, deltaY)

def walk(f,d,numSteps):
    start=f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return (start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials, dClass):
    homer=dClass('Homer')
    origin=Location(0,0)
    distances=[]
    for t in range(numTrials):
        f=Field()
        f.addDrunk(homer,origin)
        distances.append(walk(f,homer, numSteps))
    return distances

"""
def simWalks(numSteps, numTrials):
    homer=UsualDrunk('Homer')
    origin=Location(0,0)
    distances=[]
    for t in range(numTrials):
        f=Field()
        f.addDrunk(homer,origin)
        distances.append(walk(f,homer, numSteps))
    return distances
"""


def drunkTest(numTrials=20):
    random.seed(0)
    for numSteps in [10,100,1000,10000,100000]:
    #for numSteps in [0,1]:
        distances=simWalks(numSteps, numTrials)
        print 'Random walk of'+ str(numSteps) + ' steps'
        print ' Mean=',sum(distances)/len(distances)
        print ' Max=', max(distances),'Min=',min(distances)


import pylab

## #set line width
## pylab.rcParams['lines.linewidth'] = 6
## #set font size for titles
## pylab.rcParams['axes.titlesize'] = 20
## #set font size for labels on axes
## pylab.rcParams['axes.labelsize'] = 20
## #set size of numbers on x-axis
## pylab.rcParams['xtick.major.size'] = 5
## #set size of numbers on y-axis
## pylab.rcParams['ytick.major.size'] = 5
## #set size of markers
## pylab.rcParams['lines.markersize'] = 10

def drunkTestP(numTrials=50):
    stepsTaken = [10,100,1000,10000,100000]
    for dClass in (UsualDrunk, ColdDrunk, EDrunk):
        meanDistances=[]
        for numSteps in stepsTaken:
            distances=simWalks(numSteps, numTrials, dClass)
            meanDistances.append(sum(distances)/len(distances))
        pylab.plot(stepsTaken, meanDistances, label=dClass.__name__)
        pylab.title('Mean Distance from Origin')
        pylab.xlabel('Steps Taken')
        pylab.ylabel('Steps from Origin')
        pylab.legend(loc = 'upper left')
    pylab.show()

"""
def drunkTestP(numTrials = 50):
    stepsTaken=[10,100,1000,10000]
    meanDistances=[]
    for numSteps in stepsTaken:
        distances=simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken, meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()
"""

def drunkTestP1(numTrials = 50):
    stepsTaken=[10,100,1000,10000]
    meanDistances=[]
    squareRootOfSteps=[]
    for numSteps in stepsTaken:
        distances=simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken, meanDistances,'b-,',label='Mean distance')
    pylab.plot(stepsTaken, squareRootOfSteps, 'g-,',label='Square root of steps')
    
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend()
    pylab.show()
