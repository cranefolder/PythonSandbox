# -*- coding: utf-8 -*-
# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expandhelper = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    #step = 0

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    #expandhelper[init[0]][init[1]] = step

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            #expandhelper[x][y] = step
            #step += 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i # keep track of how we got to each expansion cell

    x = goal[0]
    y = goal[1]
    expand[x][y] = '*'

    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        expand[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2

    # My original solution looked at each possible backwards step.  Less efficient
    #step = expandhelper[x][y]
    #while (step > 0):
        #nextstep = step
        #for i in range(len(delta)):
            #x2 = x - delta[i][0]
            #y2 = y - delta[i][1]
            #if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                #if expandhelper[x2][y2] < nextstep and expandhelper[x2][y2] > -1:
                    #nextstep = expandhelper[x2][y2]
                    #nextx = x2
                    #nexty = y2
                    #d = i
        #x = nextx
        #y = nexty
        #expand[x][y] = delta_name[d]
        #step = nextstep
    #

    return expand # make sure you return the shortest path


result = search(grid,init,goal,cost)
if (result == 'fail'):
    print(result)
else:
    print(result[0])
    print(result[1])
    print(result[2])
    print(result[3])
    print(result[4])
