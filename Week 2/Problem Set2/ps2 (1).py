# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using
# Python 2.7 and using most likely Python 2.6:

anim = ps2_visualize.RobotVisualization(num_robots, width, height)
# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width=width
        self.height=height
        self.room={}
        for w in range(width):
            for h in range(height):
                self.room[(w,h)]=False
        #raise NotImplementedError

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under x=xx,y=yythe position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """

        
        ax = int(math.floor(pos.getX()))
        ay = int(math.floor(pos.getY()))
        self.room[(ax,ay)]=True
        #raise NotImplementedError

        '''xx,yy=pos
        a=Position()

        ax = int(math.floor(a.getX()))
        ay = int(math.floor(a.getY()))

        
        print 'before'+ str(self.room)
        self.room[(ax,ay)]=True
        print 'after'+ str(self.room)
        #raise NotImplementedError
'''
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if self.room[(m,n)]==True:
            return True
        else:
            return False
        #raise NotImplementedError

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height
        #raise NotImplementedError

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count=0
        for tile in self.room:
            if self.room[tile]==True:
                count+=1
        
        return count
        #raise NotImplementedError

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return (Position(random.randrange(self.width),random.randrange(self.height)))
        
        '''
# MY CODE
        while(True):
                
            angle=random.randint(0,360)
            
            
            speed=1

            x=random.randrange(0,self.width)
            y=random.randrange(0,self.height)
            
            new_pos=Position(x,y).getNewPosition(angle,speed)
            if new_pos.getX()>=0 and new_pos.getX()<self.width \
               and new_pos.getY()<self.height and new_pos.getY()<self.height:
                return new_pos
    
        #raise NotImplementedError
# MY CODE
    '''
    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.getX()<=self.width and 0<=pos.getX() and pos.getY()<=self.height and 0<=pos.getY():
            return True
        else:
            return False
        #raise NotImplementedError


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room=room
        self.speed=speed
        self.direct=random.randrange(360)
        self.pos=Position(random.randrange(room.width),random.randrange(room.height))
        self.room.cleanTileAtPosition(self.pos)
        
        #raise NotImplementedError

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
        #raise NotImplementedError

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direct
        #raise NotImplementedError

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos=position
        #raise NotImplementedError

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direct=direction
        #raise NotImplementedError
    '''
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        raise NotImplementedError # don't change this!
    '''

# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
         
        pos=self.getRobotPosition()
        self.room.cleanTileAtPosition(pos)
        #print pos
        new_position=Position(pos.getX(),pos.getY()).getNewPosition(self.direct, self.speed)
        #print new_position
        if self.room.isPositionInRoom(new_position):
            self.setRobotPosition(new_position)
            #print str(self.direct)
        else:
            #self.direct=self.direct+85
            while(not self.room.isPositionInRoom(new_position)):
                self.direct=random.randrange(360)
                new_position=Position(self.getRobotPosition().getX(),self.getRobotPosition().getY()).getNewPosition(self.direct, self.speed)
            #new_position=Position(pos.getX(),pos.getY()).getNewPosition(self.direct, self.speed)
            #self.setRobotPosition(new_position)
        '''
        # show the inital state of robot position
        print 'evvel: '+ str(self.getRobotPosition())

        # control and act of the position in the room
        if self.room.isPositionInRoom(self.getRobotPosition()):
            print 'a'
            #if not self.room.isTileCleaned(int(self.getRobotPosition().getX()), int(self.getRobotPosition().getY())):
            self.room.cleanTileAtPosition(self.getRobotPosition())

            # change the position to continue to lean the rest of the room
            pos=self.getRobotPosition()
            new_position=Position(pos.getX(),pos.getY()).getNewPosition(self.direct, self.speed)
            self.setRobotPosition(new_position)

            # show the Position and the direction after the cleaning
            print self.getRobotPosition()
            print 'angle' + str(self.direct)
        else:
            self.direct=random.randrange(360)

            # change the position to continue to lean the rest of the room
            #pos=self.getRobotPosition()
            #new_position=Position(pos.getX(),pos.getY()).getNewPosition(self.direct, self.speed)
            #self.setRobotPosition(new_position)
        # show the final state of robot position
        print 'sonra: ' + str(self.getRobotPosition()) + '\n'
        
        #raise NotImplementedError
        '''
# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


    
# === Problem 3
'''
def robot_type(type):
    if type=='StandardRobot':
        return StandarRobot()
    if tyoe=='RandomWalkRobot':
        return RandomWalkRobot()
'''

    
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    
    time_steps=0
    counters={}
    robots={}
    run_robot={}
    room=RectangularRoom(width,height)
     # autatic created robots
    print str(width)
    print str(height)
    print str(min_coverage)
    print 'trial: ' + str(num_trials)
    for counter in range(num_trials):
        counters[counter]=0
        
    for i in range(num_trials):
        while room.getNumCleanedTiles() < min_coverage * room.getNumTiles():
            anim.update(room, robots)
            for num in range(num_robots):
                robots[num]=robot_type(room,speed)
                robots[num].updatePositionAndClean()
                print room.getNumCleanedTiles(),
            counters[i]+=1
        
        for w in range(width):
            for h in range(height):
                room.room[(w,h)]=False
            #print 'clean tiles: ' + str(room.getNumCleanedTiles())
    time_steps=sum(counters.values())/len(counters)
    print 'time_s'
    print time_steps
    print counters
    return time_steps
    #raise NotImplementedError
    
# Uncomment this line to see how much your simulation takes on average
#print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)
anim.done()

# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        pos=self.getRobotPosition()
        self.room.cleanTileAtPosition(pos)
        #print pos
        self.direct=random.randrange(360)
        new_position=Position(pos.getX(),pos.getY()).getNewPosition(self.direct, self.speed)
        #print new_position
        if self.room.isPositionInRoom(new_position):
            self.setRobotPosition(new_position)
            #print str(self.direct)
        else:
            #self.direct=self.direct+85
            while(not self.room.isPositionInRoom(new_position)):
                self.direct=random.randrange(360)
                new_position=Position(self.getRobotPosition().getX(),self.getRobotPosition().getY()).getNewPosition(self.direct, self.speed)
        #raise NotImplementedError


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
