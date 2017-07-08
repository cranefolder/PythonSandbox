from math import *


class CircleSegment:

    def __init__(self, xcoor, ycoor, rad):
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.rad = rad

class LineSegment:

    def __init__(self, xstart, ystart, xend, yend):
        self.xstart = xstart
        self.ystart = ystart
        self.xend = xend
        self.yend = yend


    def collideswithsegment(self, othersegment):
        min_distance_to_intercept = 1.e6
        eps = 1.0e-6
        dst = 1.0e6
        #intersection = (0.,0.)

        r = self.xend-self.xstart, self.yend-self.ystart
        s = othersegment.xend-othersegment.xstart, othersegment.yend-othersegment.ystart
        qmp = othersegment.xstart-self.xstart, othersegment.ystart-self.ystart
        rxs   = r[0]*s[1] - r[1]*s[0]
        qmpxr = qmp[0]*r[1] - qmp[1]*r[0]

        if abs(rxs) >= eps :
            t = (qmp[0]*s[1] - qmp[1]*s[0])/rxs
            u = qmpxr/rxs
            if (0.0 <= t <= 1.0) and (0.0 <= u <= 1.0) :
                dx, dy = t*r[0], t*r[1]
                dst = sqrt( dx*dx + dy*dy)
                #intersection =  (self.xstart + dx, self.ystart + dy)

        collide = dst < min_distance_to_intercept
        if not collide:
            #print intersection
            collide = collide

        return collide




    def collideswithcircle(self, circlesegment):
        dstart = sqrt((circlesegment.xcoor - self.xstart) ** 2 + (circlesegment.ycoor - self.ystart) ** 2)
        dend = sqrt((circlesegment.xcoor - self.xend) ** 2 + (circlesegment.ycoor - self.yend) ** 2)

        if dstart < circlesegment.rad:
            print 'start point in circle'
            collide = True
        elif dend < circlesegment.rad:
            print 'end point in circle'
            collide = True
        else:
            x_diff = self.xend - self.xstart
            y_diff = self.yend - self.ystart
            num = abs(y_diff*circlesegment.xcoor - x_diff*circlesegment.ycoor + self.xend*self.ystart - self.yend*self.xstart)
            den = sqrt(y_diff**2 + x_diff**2)
            d = num / den
            if (d <= circlesegment.rad):
                xmin = min(self.xstart,self.xend)
                xmax = max(self.xstart,self.xend)
                ymin = min(self.ystart,self.yend)
                ymax = max(self.ystart,self.yend)
                if (xmin <= circlesegment.xcoor <= xmax) or (ymin <= circlesegment.ycoor <= ymax):
                    print 'too close:' + str(d) + ' den:' + str(den)
                    collide = True
                else:
                    print ' xmin:' + str(xmin) + ' xmax:' + str(xmax) + ' ymin:' + str(ymin) + ' ymax:' + str(ymax)
                    collide = False
            else:
                collide = False

        return collide

PI = pi
goalchar = '@'
freechar = '.'
cantraverse = [freechar,goalchar]
proxfactor = 0.45
measurelimit = 4.5
lmdirname = ['N','S','W','E']

def heading_between(p1, p2):
    return atan2(p2.ycoor - p1.ycoor, p2.xcoor - p1.xcoor)

def heading_delta(hfrom, hto):
    #if (hfrom >= 0.0 and hto >= 0.0) or (hfrom <= 0.0 and hto <= 0.0):
    hdelta = hto - hfrom
    if hdelta > pi:
        hdelta += (-2.0 * pi)
    elif hdelta < (-1.0 * pi):
        hdelta += (2.0 * pi)

    return hdelta

def angle_between(p1, p2):
    return acos((p1.xcoor*p2.xcoor + p1.ycoor*p2.ycoor) / (sqrt(p1.xcoor**2 + p1.ycoor**2) * sqrt(p2.xcoor**2 + p2.ycoor**2)))

def distance_between(point1, point2):
    return sqrt((point2.xcoor - point1.xcoor) ** 2 + (point2.ycoor - point1.ycoor) ** 2)

def getnewlocation(location, h, d):
    # Use the current heading, current turning angle, distance traveling
    # each step and current position to calculate the next position
    new_x = (cos(h) * d) + location.xcoor
    new_y = (sin(h) * d) + location.ycoor
    return MapPoint(new_x, new_y)

def getnewpoint(location, orientation, h, d):
    # Use the current heading, current turning angle, distance traveling
    # each step and current position to calculate the next position
    new_x = (cos(h + orientation) * d) + location.xcoor
    new_y = (sin(h + orientation) * d) + location.ycoor
    return RealPoint(new_x, new_y)


def getxydeltas(orientation, h, d):
    # Use the bearing and distance to find the x delta and y delta
    xdelta = (cos(h + orientation) * d)
    ydelta= (sin(h + orientation) * d)
    return xdelta, ydelta

def print2Dlist(list):
    for i in range(len(list)):
        print list[i]

def pathstring(action, x, y):
    return action + ' ' + str(y) + ' ' + str(x)

def pathstringpoint(action, point):
    return pathstring(action, point.x, point.y)


class RealPoint:

    def __init__(self, x, y):
        self.xcoor = x
        self.ycoor = y
        self.x = abs(int(self.xcoor))
        self.y = abs(int(self.ycoor))
        self.xmid = self.x + 0.5
        self.ymid = (-1.0 * self.y) - 0.5
        self.xlow = 1.0 * self.x
        self.ylow = (-1.0 * self.y)
        self.xhigh = self.xlow + 1.0
        self.yhigh = self.ylow - 1.0


    def show(self, txt = 'point'):
        print txt + ' (xcoor,ycoor): (' + str(self.xcoor) + ', ' + str(self.ycoor) + ')'

class MapPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xcoor = x + 0.5
        self.ycoor = -1.0 * (y + 0.5)
        self.xmid = self.x + 0.5
        self.ymid = (-1.0 * self.y) - 0.5
        self.xlow = 1.0 * self.x
        self.ylow = (-1.0 * self.y)
        self.xhigh = self.xlow + 1.0
        self.yhigh = self.ylow - 1.0

    def show(self, txt = 'point'):
        print txt + ': (' + str(self.x) + ', ' + str(self.y) + ')'

    def showactual(self, txt = 'point'):
        print txt + ': (' + str(self.xcoor) + ', ' + str(self.ycoor) + ')'

    def showall(self, txt = 'point'):
        print txt + ' (x,y): (' + str(self.x) + ', ' + str(self.y) + ')'
        print txt + ' (xcoor,ycoor): (' + str(self.xcoor) + ', ' + str(self.ycoor) + ')'
        print txt + ' (xmid,ymid): (' + str(self.xmid) + ', ' + str(self.ymid) + ')'
        print txt + ' (xlow,ylow): (' + str(self.xlow) + ', ' + str(self.ylow) + ')'
        print txt + ' (xhigh,yhigh): (' + str(self.xhigh) + ', ' + str(self.yhigh) + ')'



"""

West OOPS!!  rl:(3.10146971341, -2.61971253329) rawpx:0.601469713403 rawpy:-2.61971253328 xd:-1.22411659887e-11 yd:-2.50000000001
measure: ('warehouse', 2, 2.500000000009793, -1.570796326799793)
"""

measurement = ('warehouse', 2, 2.500000000009793, -1.570796326799793)
robotlocation = RealPoint(2.5, -1.5)
robotorienation = -PI/2
landmarkindex = -1
lmtype = measurement[0]
lmdir = lmdirname[measurement[1]]
lmdistance = measurement[2]
lmbearing = measurement[3]

lmrawpoint = getnewpoint(robotlocation, robotorienation, lmbearing, lmdistance)
xdelta, ydelta = getxydeltas(robotorienation, lmbearing, lmdistance)

print 'rl:(' + str(robotlocation.xcoor) + ', ' + str(robotlocation.ycoor) +  ')'
print 'rawpx:' + str(lmrawpoint.xcoor) + ' rawpy:' + str(lmrawpoint.ycoor)
print 'xd:' + str(xdelta) + 'yd:' + str(ydelta)

