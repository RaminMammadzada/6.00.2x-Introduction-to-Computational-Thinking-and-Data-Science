class RectangularRoom(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.room = [[0 for i in range(self.width)] for i in range(self.height)]


    def cleanTileAtPosition(self, pos):
        self.room[int(pos.getY())][int(pos.getX())] = 1 # clean

    def isTileCleaned(self, m, n):
        return self.room[n][m]

    def getNumTiles(self):
        return len(self.room)*len(self.room[0])

    def getNumCleanedTiles(self):
        return sum([sum(self.room[i]) for i in range(self.height)])

    def getRandomPosition(self):
        return (Position(random.randrange(self.width),random.randrange(self.height)))

    def isPositionInRoom(self, pos):
        return (True if 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height else False)


def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5