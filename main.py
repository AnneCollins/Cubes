#!/usr/bin/env python

''' The snake is made of segments of given length, that have to be at right
angle  from each other (either clockwise or counterclockwise). Segments are
solid, they can't overlap. 
The target shape is a rectangle, specified by width and length. 
We want to orient the segments of the snake so that it covers exactly the target
shape. '''


import json
import sys

class Snake(object):
    def __init__(self, segment_lengths):
        print "Construct!"
        self.lengths = [int(sl) for sl in segment_lengths]

    def print_me(self):
        print self.lengths


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
    s = Snake(args)
    s.print_me()

    rectangle = Shape(3,4)
    print(rectangle)

if __name__ == "__main__":
    main(sys.argv[1:])
