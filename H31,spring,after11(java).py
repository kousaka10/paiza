class Maze():
    def __init__(self, mazeData, width):
        self.mazeData = mazeData
        self.width = int(width)
        self.startLocation = self.location0f('S')

    def getStartLocation(self):
        return self.startLocation
    
    def isGoal(self, loc):
        return self.mazeData[loc.y * self.width + loc.x] == 'G'
    
    def isBlank(self, loc):
        return self.mazeData[loc.y * self.width + loc.x] == '*'
    
    def location0f(self, c):
        index = self.mazeData.index(c)
        return Location(index % self.width, index // self.width)

    
from enum import Enum

class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __init__(self, dx, dy):
        self.dx = int(dx)
        self.dy = int(dy)
        self.values = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def left(self):
        order = self.values.index(Direction((self.dx, self.dy)).name)
        return (Direction[self.values[(order + 3) % 4]])

    def right(self):
        order = self.values.index(Direction((self.dx, self.dy)).name)
        return (Direction[self.values[(order + 1) % 4]])
    
    def __repr__(self):
        return Direction((self.dx, self.dy)).name


class Location():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    
class Piece():
    def __init__(self, maze):
        self.history = []
        self.direction = Direction.NORTH
        self.maze = maze
        self.location = self.maze.getStartLocation()

    def turnLeft(self):
        self.direction = self.direction.left()

    def turnRight(self):
        self.direction = self.direction.right()
    
    def tryStepForward(self):
        nextLocation = Location(self.location.x + self.direction.dx, self.location.y + self.direction.dy)
        if self.maze.isBlank(nextLocation):
            self.location = nextLocation
            self.history.append(self.direction)
            return True
        return False

    def isAtGoal(self):
        return self.maze.isGoal(self.location)

    def getHistory(self):
        return self.history


maze = Maze("*******" +
            "*..*..*" +
            "*S**.**" +
            "*.....*" +
            "*****.*" +
            "*G....*" +
            "*******", 7)

piece = Piece(maze)
while not piece.isAtGoal():
    piece.turnLeft()
    while not piece.tryStepForward():
        piece.turnRight()

history = piece.getHistory()

i = 1
while i < len(history):
    if history[i-1] == history[i].left().left():
        history.pop(i-1)
        history.pop(i-1)
        i = 0 if i < 2 else i - 2
    i += 1

print(history)