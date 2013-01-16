#!/usr/bin/env python

''' The snake is made of segments of given length, that have to be at right
angle  from each other (either clockwise or counterclockwise). Segments are
solid, they can't overlap.  If the snake is [2, 2, 1], then, the first segment
is length 3, second segment is length 3, third segment is length 2
***0
00*0
00**
So it's equivalent to [1, 2, 2], in reverse.

The target shape is a rectangle, specified
by width and length.  We want to orient the segments of the snake so that it
covers exactly the target shape. '''


import itertools
import json
import sys

import draw

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



class Snake(object):
    def __init__(self, segment_lengths):
        self.lengths = [int(sl) for sl in segment_lengths]

    def print_me(self):
        print self.lengths

    def configuration(self, turns):
        ''' this is going to configure the snake in n-d
        given segment lengths and list of oriented angles between the segments

        if the snake would intercept itself, return an Overlap exception
        if it doesn't overlap, return shape.

        First segment always goes horizontally (from coordinates [0, 0] to 
            [length-1,0]), then turns specify left or right turns.

        '''
        head = (0, 0, 0)
        conf = set([head])
        d = Direction(1, 0, 0)

        #step first, then turn (so dummy turn at the end doesn't matter)
        for length, turn in zip(self.lengths, turns+[Rotation.CLOCKWISE]):
            for step in range(length):
                next = d.step(head)

                #print "Head is {1}, Next is {0}, dir={2} turn={3}".format(next, head, d, turn)
                if next in conf:
                    raise OverlapException('Overlap at {0}'.format(next))

                conf.add(next)
                head = next

            d.turn(turn)

        return conf

def makeCanonical(conf):
    '''takes a configuration, returns the same configuration translated so that it fits in
    the top right quadrant'''
    xs = [point[0] for point in conf]
    ys = [point[1] for point in conf]
    zs = [point[2] for point in conf]

    mx = min(xs)
    xs = [x - mx for x in xs]

    my = min(ys)
    ys = [y - my for y in ys]

    mz = min(zs)
    zs = [z - mz for z in zs]

    diameter = max([max(zs), max(xs),max(ys)]);
    if diameter<4:

        print("Diameter is {0}".format(diameter))

    return set(zip(xs, ys, zs))



class OverlapException(Exception):
    pass

class Shape(object):
    def __init__(self, length, width, depth):
        #print "Construct!"
        self.length = length
        self.width = width
        self.depth = depth
        # HACK! check more possible rotations of the shape
        self.coordinatesW = set(itertools.product(range(self.width), range(self.length), range(self.depth))) 
        self.coordinatesL = set(itertools.product(range(self.length), range(self.depth), range(self.width))) 
        self.coordinatesD = set(itertools.product(range(self.depth), range(self.width), range(self.length))) 


    def __str__(self):
        return 'Shape(len = {0}, wid = {1}), dep = {2}'.format(self.length, self.width, self.depth)

    def compare(self, conf):
        ''' Compare configuration and shape. Returns True if they match.'''

        conf = makeCanonical(conf)
        #print(conf)
        return (conf == self.coordinatesW) or (conf == self.coordinatesL) or (conf == self.coordinatesD)




def main(args):

    print "Welcome to the Cube Solver!!!"
    print args

    puzzle = json.load(open(args[0]))

    s = Snake(puzzle["snake"])
    dims = puzzle["shape"]
    rectangle = Shape(dims["len"], dims["wid"], dims["dep"])

    #print(rectangle)
    N = len(s.lengths)
    # HACK!


    result = 'fail'
    successfulturns = 0
    for  turns in itertools.product([1, 2, 3, 4],repeat = N-1):
        #print(turns)
        try:
            conf = s.configuration(list(turns))
            if rectangle.compare(conf):
                print('here is a sequence of turns that solves the puzzle: ')
                print(turns)
                result = success
                successfulturns = turns
#                draw.draw_configuration(makeCanonical(conf), rectangle)
            # check whether configuration and shape match
            # if so interrupt, draw, return sequence of turns


        except OverlapException:
            pass


    print(successfulturns)
    print(result)

#def testCompare():

#def testMakeCanonical():


if __name__ == "__main__":
#    testCompare()
#    testMakeCanonical()
    main(sys.argv[1:])

