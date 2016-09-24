#!/usr/bin/env python
import pprint as pp


def knapsack(capacity, items):
    # Define table
    t = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(t[:])):
        for j in range(1, len(t[:][i])):
            w = items[i - 1][0]
            v = items[i - 1][1]
            w_add = j - w
            v_over = t[i - 1][j]

            if w <= j and v + t[i - 1][w_add] > v_over:
                t[i][j] = v + t[i - 1][w_add]
            else:
                t[i][j] = v_over

    pp.pprint(t)


knapsack(8, [(1, 15), (5, 10), (3, 9), (4, 5)])
