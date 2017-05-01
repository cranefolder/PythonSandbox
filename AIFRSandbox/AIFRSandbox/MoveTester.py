# -*- coding: utf-8 -*-
def moveTthomas82(p, motion, p_move):
    q = []
    yDelta = motion[0]
    xDelta = motion[1]
    for r in range(len(p)):
        qr = []
        for c in range(len(p[0])):
            # s = p_move *
            s = p_move * p[(r - yDelta) % len(p)][(c - xDelta) % len(p[0])]
            s += (1 - p_move) * p[r][c]
            qr.append(s)
        q.append(qr)
    return q


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


def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print ('[' + ',\n '.join(rows) + ']')
    print ('                   ')


# final test
p = [[0.0,0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 1.11111, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0]]

#motions = [[0,1],[1,0],[0,-1],[-1,0]]
motions = [[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],[0,-1]]

p_move = 1.0 #0.8

show(p)
for i in range(len(motions)):
    p = moveTthomas82(p,motions[i], p_move)
    show(p)

