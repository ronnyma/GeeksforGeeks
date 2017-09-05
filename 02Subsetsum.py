#!/usr/bin/env python
import random as rnd
import sys


def subset_sum(sum, set):
    t = [[0 if x != 0 else 1 for x in range(sum + 1)] for y in range(len(set))]

    for i in range(len(t[:])):
        for j in range(len(t[i][:])):
            num = set[i]
            t[i][j] = t[i - 1][j] if t[i - 1][j] else t[i - 1][j - num]

    return t[-1][-1]


if __name__ == "__main__":
    num = int(sys.argv[1])
    d = [x * rnd.randint(1, 1000) for x in range(1, num+1)]
    s = sum(d)
    print len(d), s / 2
    if subset_sum(s / 2, d):
        print "Exists!"
    else:
        print "Not possiblei."
