# -*- coding: utf-8 -*-
# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right

goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    value = [[[999 for col in range(len(grid[0]))] for row in range(len(grid))]
            ,[[999 for col in range(len(grid[0]))] for row in range(len(grid))]
            ,[[999 for col in range(len(grid[0]))] for row in range(len(grid))]
            ,[[999 for col in range(len(grid[0]))] for row in range(len(grid))]]

    y = init[0]
    x = init[1]
    d = init[2]
    g = 0
    value[d][y][x] = g

    open = [[g, y, x, d, policy2D]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            g = next[0]
            y = next[1]
            x = next[2]
            d = next[3]
            policy2D = [r[:] for r in next[4]] #needed to make a true copy
            #print('------------------------------------------------')
            #print(next[0:4])
            #print2dlist(policy2D)

            if x == goal[1] and y == goal[0]:
                found = True
                policy2D[y][x] = '*'
                #print(path)
            else:
                for a in range(len(action)):
                    d2 = (d + action[a]) % len(forward)
                    motion = forward[d2]
                    y2 = y + forward[d2][0]
                    x2 = x + forward[d2][1]
                    g2 = g + cost[a]
                    policy2D2 = [r[:] for r in policy2D] #needed to make a true copy
                    if x2 >= 0 and x2 < len(grid[0]) and y2 >=0 and y2 < len(grid):
                        if value[d2][y2][x2] > g2 and grid[y2][x2] == 0:
                            #print('a:' + str(a) + ' cost:' + str(cost[a]))
                            policy2D2[y][x] = action_name[a]
                            open.append([g2, y2, x2, d2, policy2D2])
                            value[d2][y2][x2] = g2
        #print3dlist(value)
        #print2dlist(policy2D)

    return policy2D

def print3dlist(i):
    print('------------------------------------------------------------')
    for r in range(len(i[0])):
        s = '['
        for a in range(len(i)):
            if a > 0:
                s += ']     ['
            for c in range(len(i[0][0])):
                if c == 0:
                    s += str(i[a][r][c]).rjust(3)
                else:
                    s += ',' + str(i[a][r][c]).rjust(5)
        print(s + ']')
    print('')

def print2dlist(i):
    #print('--------------    Policy              ----------------------')
    for r in range(len(i)):
        s = '['
        for c in range(len(i[0])):
            if c == 0:
                s += str(i[r][c]).rjust(3)
            else:
                s += ',' + str(i[r][c]).rjust(5)
        print(s + ']')
    print('')


result = optimum_policy2D(grid,init,goal,cost)
if (result == 'fail'):
    print(result)
else:
    print2dlist(result)