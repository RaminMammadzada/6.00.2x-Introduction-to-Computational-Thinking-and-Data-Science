import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result=''
    for i in range(n):
        result = result + str(rollDie())
    return result

#print rollN(5)

def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries +=1
        result = rollN(numRolls)
        if result==goal:
            return numTries

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        total += getTarget(goal)
    aveNumTries = total/float(numTrials)
    print 'Probability = ', 1.0/aveNumTries

runSim('11111', 100)
runSim('54324', 100)
