#!/usr/bin/python3
import sys
import ctypes

def print_factors():
    with open(sys.argv[1], 'r') as prime:
        line = prime.readline()
        while line != '':
            n = int(line)
            fun.trial_division(n)
            line = prime.readline()
