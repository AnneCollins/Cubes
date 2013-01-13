#!/usr/bin/env python
import json
import sys

class Direction(object):
    CLOCKWISE = 0
    COUNTER = 1

class Shape(object):
    def __init__(self, x):
        print "Construct!"
        self.x = x

    def print_me(self):
        print self.x

def main(args):
    print "Welcome to the Cube Solver!!!"
    print args
    s = Shape(args[0])
    s.print_me()

if __name__ == "__main__":
    main(sys.argv[1:])

