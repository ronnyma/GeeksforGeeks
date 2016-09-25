#!/usr/bin/env python
import pprint as pp


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
    d = [(2, 74), (5, 72), (8, 378), (5, 488), (14, 360), (15, 594), (20, 672), (3, 100), (13, 656), (38, 108),
         (32, 38), (10, 129), (2, 336), (18, 120), (50, 384), (18, 168), (28, 168), (15, 12), (45, 72), (6, 267),
         (48, 348), (51, 305), (21, 612), (45, 504), (69, 528), (76, 87), (96, 142), (40, 336), (76, 388), (72, 735),
         (16, 276), (44, 819), (16, 856), (95, 71), (100, 128), (45, 231), (45, 496), (20, 510), (110, 558), (20, 798),
         (35, 1128), (108, 109), (138, 272), (42, 39), (12, 368), (96, 410), (114, 672), (138, 336), (42, 168),
         (35, 120), (105, 284), (161, 348), (140, 84), (98, 720), (35, 606), (14, 399), (133, 1072), (176, 25),
         (56, 58), (136, 231), (112, 548), (16, 600), (32, 894), (152, 973), (72, 272)]

    knapsack(500, d)
