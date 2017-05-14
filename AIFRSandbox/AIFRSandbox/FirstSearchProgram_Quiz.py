# -*- coding: utf-8 -*-
# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    # set initial path to length of zero and starting coordinates of init
    path = [0, init[0], init[1]]
    paths = []
    paths.append([path[0], path[1], path[2], 0])
    expandedpos = 3
    xmax = len(grid[0]) - 1
    ymax = len(grid) - 1
    np = 0

    # see if we are at the goal, or
    while (path[1] != goal[0] or path[2] != goal[1]) and (np >= 0):
        #print ('Starting loop for [c=%s, y=%s, x=%s]' % (str(path[0]),str(path[1]),str(path[2])))

        # add all possible expansions that are valid and haven't already been added
        for i in range(len(delta)):
            newpos = [path[1] + delta[i][0], path[2] + delta[i][1]]
            # no negative x or y values, no exceeding grid size
            if newpos[0] >= 0 and newpos[0] <= ymax and newpos[1] >= 0 and newpos[1] <= xmax:
               #no moving to Occupied spaces,
                if grid[newpos[0]][newpos[1]] == 0:
                    #no dupes
                    dupe = False
                    for j in range(len(paths)):
                        if paths[j][1] == newpos[0] and paths[j][2] == newpos[1]:
                            dupe = True
                    if not dupe:
                        paths.append([path[0] + cost, newpos[0], newpos[1], 0])

        # find smallest path that hasn't been expanded yet
        mincost = -1
        np = -1
        for p in range(len(paths)):
            # when we find our current path, mark it as expanded
            if paths[p][1] == path[1] and paths[p][2] == path[2]:
                paths[p][expandedpos] = 1
            # if the path has not yet been expanded, look at the cost and see
            # if it is lower than current lowest cost
            if paths[p][expandedpos] == 0:
                if paths[p][0] < mincost or mincost == -1:
                    mincost = paths[p][0]
                    np = p

        # if we found a new path, try that on the next loop, else return 'fail'
        if (np >= 0):
            path = [paths[np][0], paths[np][1], paths[np][2]]
        else:
            path = 'fail'

    return path

'''--------  Below is for debugging and showing results only --------------- '''
result = search(grid, init, goal, cost)
print('-------  Finished ----------')
print(result)