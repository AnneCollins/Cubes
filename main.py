#!/usr/bin/env python

''' The snake is made of segments of given length, that have to be at right
angle  from each other (either clockwise or counterclockwise). Segments are
solid, they can't overlap.  If the snake is [3, 2, 1], then, the first segment
is length 3, second segment is length 3, third segment is length 2
***0
00*0
00**
So it's equivalent to [2, 2, 2], in reverse

The target shape is a rectangle, specified
by width and length.  We want to orient the segments of the snake so that it
covers exactly the target shape. '''


import json
import sys


class Direction(object):
    CLOCKWISE = 0
    COUNTER = 1


class Snake(object):
    def __init__(self, segment_lengths):
        self.lengths = [int(sl) for sl in segment_lengths]

    def print_me(self):
        print self.lengths

    def configuration(self, turns):
        ''' this is going to configure the snake in n-d
        given segment lengths and list of oriented angles between the segments
        '''
        


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
    s.print_me()
    dims = puzzle["shape"]
    rectangle = Shape(dims["len"], dims["wid"])
    print(rectangle)




if __name__ == "__main__":
    main(sys.argv[1:])

