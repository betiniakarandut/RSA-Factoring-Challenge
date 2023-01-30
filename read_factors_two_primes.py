#!/usr/bin/python3
import sys

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp


def unix_time(function):
    '''Return `real`, `sys` and `user` elapsed time, like UNIX's command `time`
    You can calculate the amount of used CPU-time used by your
    function/callable by summing `user` and `sys`. `real` is just like the wall
    clock.
    Note that `sys` and `user`'s resolutions are limited by the resolution of
    the operating system's software clock (check `man 7 time` for more
    details).
    '''
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()

    return "\nreal: {}\nuser: {}\nsys: {}\n".format(
        end_time - start_time,
        end_resources.ru_utime - start_resources.ru_utime,
        end_resources.ru_stime - start_resources.ru_stime)


def trial_division(x: int) -> int:
    """
    Finds the smallest divisor, if any, of a given number `x`
    Returns:
        smallest divisor if found
        0 if n is prime
    """
    # TODO: Create a C library with this function to speed it up
    prime_factors = []
    divisor = 2
    n = x

    while divisor <= x:
        if x % divisor == 0:
            prime_factors.append(divisor)
            x = x / divisor
        else:
            divisor += 1   # divisor = divisor + 1
    p = prime_factors[0]
    q = prime_factors[1]
    return ("{}={}*{}".format(n, p, q))


def print_factors():
    """Prints result read from commandline.

    Args:
        None

    Return:
        Nothing
    """

    with open(sys.argv[1], 'r') as prime:
        line = prime.readline()
        while line != '':
            x = int(line)
            rep = trial_division(x)
            print(rep)

            line = prime.readline()
