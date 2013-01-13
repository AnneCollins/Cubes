#!/usr/bin/env python
import json
import sys

class Snake(object):
    def __init__(self, segment_lengths):
        print "Construct!"
        self.lengths = [int(sl) for sl in segment_lengths]

    def print_me(self):
        print self.lengths

def main(args):
    print "Welcome to the Cube Solver!!!"
    print args
    s = Snake(args)
    s.print_me()

if __name__ == "__main__":
    main(sys.argv[1:])
