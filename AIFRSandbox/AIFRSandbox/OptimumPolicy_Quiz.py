# -*- coding: utf-8 -*-
# ----------
# User Instructions:
#
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
#
# Unnavigable cells as well as cells from which
# the goal cannot be reached should have a string
# containing a single space (' '), as shown in the
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    evaluated = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    x = goal[0]
    y = goal[1]
    g = 0
    toevaluate = [[g, x, y]]
    evaluated[x][y] = 1
    policy[x][y] = '*'

    while len(toevaluate) > 0:
        toevaluate.sort()
        toevaluate.reverse()
        evaluating = toevaluate.pop()
        g = evaluating[0]
        x = evaluating[1]
        y = evaluating[2]
        value[x][y] = g

        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                if evaluated[x2][y2] == 0 and grid[x2][y2] == 0:
                    g2 = g + cost
                    toevaluate.append([g2, x2, y2])
                    evaluated[x2][y2] = 1
                    policy[x2][y2] = delta_name[(i + 2) % 4]

    return policy


result = optimum_policy(grid,goal,cost)
if (result == 'Fail'):
    print(result)
else:
    print(result[0])
    print(result[1])
    print(result[2])
    print(result[3])
    print(result[4])