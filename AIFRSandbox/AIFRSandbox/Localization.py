# -*- coding: utf-8 -*-

# p represents the probability (or belief) of where we could be located in the world
p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world represents our known map of the world
world=['green', 'red', 'red', 'green', 'green']
# measurements represents the measurements we take over time
measurements = ['red','red']
# motions represents the magnitude and direction of each move we take over time
motions = [1,1]
# pHit and pMiss represent the factors that we multiply the probability of each location by after sensing
pHit = 0.6
pMiss = 0.2
# pExact, pOvershoot, pUndershoot represent the factors that we multiply the probability of each location by after moving
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# returns a new vector q, that compares the measurement Z to the world and generates the posterior probability
# the sense is a Product followed by Normalization
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        if (world[i] == Z):
            q.append(p[i] * pHit)
        else:
            q.append(p[i] * pMiss)
    #normalize the new probability vector q so it sums to 1
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

# returns a new vector q, that represents the probable location changes after moving and factoring in our Undershoot and Overshoot chances
# the move is a "Convolution"
def move(p, U):
    q = []
    for j in range(len(p)):
        s = pExact * p[(j-U) % len(p)]
        s += pOvershoot * p[(j-U-1) % len(p)]
        s += pUndershoot * p[(j-U+1) % len(p)]
        q.append(s)
    return q
''' My solution
        x = (j + U) % len(p)
        o = (j + U + 1) % len(p)
        u = (j + U - 1) % len(p)
        q[x] = q[x] + (p[j] * pExact)
        q[o] = q[o] + (p[j] * pOvershoot)
        q[u] = q[u] + (p[j] * pUndershoot)
    return q
        '''


# Process our sensor readings and movements: first sense, then move
for i in range(len(measurements)):
    p = sense(p, measurements[i])
    p = move(p,motions[i])
print(p)

