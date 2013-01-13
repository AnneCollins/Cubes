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


import json
import sys


class Rotation(object):
    CLOCKWISE = 0
    COUNTER = 1

class Direction(object):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def step(self, point):
        #returns a new point after taking a step in current direction
        newpoint = (newpoint[0]+dx, newpoint[1]+dy)
        return newpoint


    def turn(self, angle):
        #changes internal direction, returns nothing
        if angle == Rotation.CLOCKWISE:
            self.dx = self.dy
            self.dy = - self.dx
        else:
            self.dx = - self.dy
            self.dy = self.dx



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
        conf = set()
        d = Direction(1,0)
        head = (0, 0)
        #step first, then turn (so dummy turn at the end doesn't matter)
        for length, turn in zip(self.lengths, turns+[Rotation.CLOCKWISE]):
            for step in range(length):
                next = d.step(head)
                if next in conf:
                    raise Overlap('Overlap at {0}'.format(next))

                conf.add(next)

            d.turn(turn)

        return conf



class Overlap(Exception)
    pass

class Shape(object):
    def __init__(self, length, width):
        print "Construct!"
        self.length = length
        self.width = width

    def __str__(self):
        return 'Shape(len = {0}, wid = {1})'.format(self.length, self.width)



def main(args):
    print "Welcome to the Cube Solver!!!"
    print args

    puzzle = json.load(open(args[0]))

    s = Snake(puzzle["snake"])
    dims = puzzle["shape"]
    rectangle = Shape(dims["len"], dims["wid"])
    print(rectangle)




if __name__ == "__main__":
    main(sys.argv[1:])

