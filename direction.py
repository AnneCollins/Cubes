
class Rotation(object):
    CLOCKWISE = -1
    COUNTER = 1

    R3D1 = 1
    R3D2 = 2
    R3D3 = 3
    R3D4 = 4

class Direction(object):
    def __init__(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz

    def step(self, point):
        #returns a new point after taking a step in current direction
        newpoint = (point[0] + self.dx, point[1] + self.dy, point[2] + self.dz)
        return newpoint


    def turn(self, angle):
        #changes internal direction, returns nothing
        #print "Turn: " , self, angle

        if self.dx ==1 or self.dx == -1:
            if angle == 1:
                self.dx, self.dy, self.dz = 0, self.dx, 0
            elif angle == 2:
                self.dx, self.dy, self.dz = 0, 0, -self.dx
            elif angle == 3:
                self.dx, self.dy, self.dz = 0, -self.dx, 0
            else:
                self.dx, self.dy, self.dz = 0, 0, self.dx

        elif self.dy == 1 or self.dy == -1:
            if angle == 1:
                self.dx, self.dy, self.dz = self.dy, 0, 0
            elif angle == 2:
                self.dx, self.dy, self.dz = 0, 0, -self.dy
            elif angle == 3:
                self.dx, self.dy, self.dz = -self.dy, 0, 0
            else:
                self.dx, self.dy, self.dz = 0, 0, self.dy

        elif self.dz == 1 or self.dz == -1:
            if angle == 1:
                self.dx, self.dy, self.dz = self.dz, 0, 0
            elif angle == 2:
                self.dx, self.dy, self.dz = 0, self.dz, 0
            elif angle == 3:
                self.dx, self.dy, self.dz = -self.dz, 0, 0
            else:
                self.dx, self.dy, self.dz = 0, -self.dz, 0



        #if angle == Rotation.CLOCKWISE:
        #    self.dx, self.dy = self.dy, -self.dx
        #else:
        #    self.dx, self.dy = - self.dy, self.dx
        #print "result: ", self

    def __str__(self):
        return "Direction({0},{1},{2})".format(self.dx, self.dy, self.dz)

