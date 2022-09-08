EAST = 2
NORTH = 1
WEST = 4
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.coordinates = (self.x, self.y)

    def move(self, order):
        for n in order:
            if n == 'R':
                self._right()
            elif n == 'L':
                self._left()
            elif n == 'A':
                self._advance()
        self.coordinates = (self.x , self.y)   

    def _right(self):
        self.direction += 1
        if self.direction == 5:
            self.direction-=4

    def _left(self):
        self.direction -= 1
        if self.direction == 0:
            self.direction += 4
            
    def _advance(self):
        if self.direction == NORTH:
            self.y+=1
        elif self.direction == EAST:
            self.x+=1
        elif self.direction == SOUTH:
            self.y-=1
        elif self.direction == WEST:
            self.x-=1     