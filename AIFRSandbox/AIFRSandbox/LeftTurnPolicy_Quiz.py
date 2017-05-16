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

    evaluated = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

    y = init[0]
    x = init[1]
    d = init[2]
    g = 0
    value[d][y][x] = g

    #closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed = [[[0 for col in range(len(grid[0]))] for row in range(len(grid))]
            ,[[0 for col in range(len(grid[0]))] for row in range(len(grid))]
            ,[[0 for col in range(len(grid[0]))] for row in range(len(grid))]
            ,[[0 for col in range(len(grid[0]))] for row in range(len(grid))]]

    closed[d][y][x] = 1

    open = [[g, y, x, d]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail', value
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            g = next[0]
            y = next[1]
            x = next[2]
            d = next[3]

            print('------------------------------------------------')
            print(next)

            if x == goal[1] and y == goal[0]:
                found = True
            else:
                #for o in range(len(forward)):
                for a in range(len(action)):
                    d2 = (d + action[a]) % len(forward)
                    motion = forward[d2]
                    y2 = y + forward[d2][0]
                    x2 = x + forward[d2][1]
                    g2 = g + cost[a]
                    if x2 >= 0 and x2 < len(grid[0]) and y2 >=0 and y2 < len(grid):
                        #if closed[d2][y2][x2] == 0 and grid[y2][x2] == 0:
                        if value[d2][y2][x2] > g2 and grid[y2][x2] == 0:
                            print('a:' + str(a) + ' cost:' + str(cost[a]))
                            open.append([g2, y2, x2, d2])
                            value[d2][y2][x2] = g2
                            closed[d2][y2][x2] = 1
                            #action[y2][x2] = motion # keep track of how we got to each expansion cell
        print3dlist(value)
    #x = goal[1]
    #y = goal[0]
    #expand[x][y] = '*'

    #while x != init[0] or y != init[1]:
        #x2 = x - delta[action[x][y]][0]
        #y2 = y - delta[action[x][y]][1]
        #expand[x2][y2] = delta_name[action[x][y]]
        #x = x2
        #y = y2


    ##x = goal[0]
    ##y = goal[1]
    ##g = 0
    ##toevaluate = [[g, x, y]]
    ##evaluated[x][y] = 1

    ##while len(toevaluate) > 0:
        ##toevaluate.sort()
        ##toevaluate.reverse()
        ##evaluating = toevaluate.pop()
        ##g = evaluating[0]
        ##x = evaluating[1]
        ##y = evaluating[2]
        ##value[o][x][y] = g

        ##for o in range(len(forward)):
            ##for i in range(len(delta)):
                ##x2 = x + delta[i][0]
                ##y2 = y + delta[i][1]
                ##if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    ##if evaluated[x2][y2] == 0 and grid[x2][y2] == 0:
                        ##g2 = g + cost
                        ##toevaluate.append([g2, x2, y2])
                        ##evaluated[x2][y2] = 1

    #print(str(value[0][0]) + '    '  + str(value[1][0]) + '    '  + str(value[2][0]) + '    '  + str(value[3][0]))
    #print(str(value[0][1]) + '    '  + str(value[1][1]) + '    '  + str(value[2][1]) + '    '  + str(value[3][1]))
    #print(str(value[0][2]) + '    '  + str(value[1][2]) + '    '  + str(value[2][2]) + '    '  + str(value[3][2]))
    #print(str(value[0][3]) + '    '  + str(value[1][3]) + '    '  + str(value[2][3]) + '    '  + str(value[3][3]))
    #print(str(value[0][4]) + '    '  + str(value[1][4]) + '    '  + str(value[2][4]) + '    '  + str(value[3][4]))

    return policy2D, value

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


result, result2 = optimum_policy2D(grid,init,goal,cost)
print3dlist(result2)
