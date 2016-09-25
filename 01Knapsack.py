#!/usr/bin/env python
import pprint as pp
import random as rnd


def knapsack(capacity, items):
    # Define table
    t = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]
    k = [[0 for x in range(capacity)] for y in range(len(items))]

    for i in range(1, len(t[:])):
        for j in range(1, len(t[:][i])):
            w = items[i - 1][0]
            v = items[i - 1][1]
            w_add = j - w
            v_over = t[i - 1][j]

            if w <= j and v + t[i - 1][w_add] > v_over:
                t[i][j] = v + t[i - 1][w_add]
                k[i - 1][j - 1] = 1
            else:
                t[i][j] = v_over

    s = []
    l = -1
    for i in range(1, len(k) + 1):
        it = len(k) - i
        if k[-i][l] == 1:
            s.append(items[it])
            l -= items[it][0]

    pp.pprint(s)
    print "Total weight: %s\nTotal value: %s" % (sum(x[0] for x in s), sum(x[1] for x in s))


if __name__ == "__main__":
    d = [(x*rnd.randint(1,25),y*rnd.randint(10,150)) for x in range(1,25) for y in range(1,30)]
    cap = sum(x[0] for x in d)
    print "Capacity: ", cap
    knapsack(cap/2, d)
