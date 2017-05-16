# -*- coding: utf-8 -*-
# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    evaluated = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = goal[0]
    y = goal[1]
    g = 0
    toevaluate = [[g, x, y]]
    evaluated[x][y] = 1

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


    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value


result = compute_value(grid,goal,cost)
if (result == 'Fail'):
    print(result)
else:
    print(result[0])
    print(result[1])
    print(result[2])
    print(result[3])
    print(result[4])