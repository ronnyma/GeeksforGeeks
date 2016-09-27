#!/usr/bin/env python
import random as rnd


def subset_sum(sum, set):
    t = [[0 if x != 0 else 1 for x in range(sum + 1)] for y in range(len(set))]

    for i in range(len(t[:])):
        for j in range(len(t[i][:])):
            num = set[i]
            # if num == j:
            #    t[i][j] = 1
            # else:
            t[i][j] = t[i - 1][j] if t[i - 1][j] else t[i - 1][j - num]

    #pp.pprint(t)
    return t[-1][-1]


if __name__ == "__main__":
    d = [x * rnd.randint(1, 2500) for x in range(1, 2500)]
    s = sum(d)
    print len(d), s / 2
    if subset_sum(s / 2, d):
        print "Exists"
    else:
        print "Not possible"
