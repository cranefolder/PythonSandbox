from math import *

def distance_between(point1, point2):
    return sqrt((point2.xcoor - point1.xcoor) ** 2 + (point2.ycoor - point1.ycoor) ** 2)

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




    #def distancetopoint(self, px, py):

        #dst = 1.e6
        #dx = self.xend - self.xstart
        #dy = self.yend - self.ystart

        #d2 = (dx*dx + dy*dy)

        #if abs(d2) > 1.e-6:

            #t = ((px - self.xstart) * dx + (py - self.ystart) * dy)/d2

            ## if point is on line segment
            #if 0.0 <= t <= 1.0:
                #intx, inty = self.xstart + t*dx, self.ystart + t*dy
                #dx, dy = px - intx, py - inty

            ## point is beyond end point
            #elif t > 1.0 :
                #dx, dy = px - l1[0], py - l1[1]

            ## point is before beginning point
            #else:
                #dx, dy = px - self.xstart, py - self.ystart

            #dst = sqrt(dx*dx + dy*dy)

        #else:
            #dx, dy = px - self.xstart, py - self.ystart
            #dst = sqrt(dx*dx + dy*dy)


        #return dst

    #def _corner_intersection( self, t0, t1, corner ):
    #def collideswithcircle(self, circlesegment):

        #dst = 1.e6
        #intercept_point = (0.,0.)

        #a = circlesegment.xcoor
        #b = circlesegment.ycoor
        #r = circlesegment.rad

        ## check the case for infinite slope
        #dx = self.xend - self.xstart

        ## Find intersection assuming vertical trajectory
        #if abs( dx ) < 1.e-6 :
            #x0 = self.xstart - a
            ##qa = 1.
            #qb = -2.*b
            #qc = b*b + x0*x0 - r*r
            #disc = qb*qb - 4.*qc

            #if disc >= 0.:
                #sd = sqrt(disc)
                #xp = xm = self.xstart
                #yp = (-qb + sd)/2.
                #ym = (-qb - sd)/2.

        ## Find intersection assuming non vertical trajectory
        #else:
            #m = (self.yend - self.ystart)/dx # slope of line
            #c = self.ystart - m*self.xstart    # y intercept of line

            #qa = 1.+m*m
            #qb = 2.*(m*c - m*b - a)
            #qc = a*a + b*b + c*c - 2.*b*c - r*r

            #disc = qb*qb - 4.*qa*qc

            #if disc >= 0.:
                #sd = math.sqrt(disc)
                #xp = (-qb + sd) / (2.*qa)
                #yp = m*xp + c
                #xm = (-qb - sd) / (2.*qa)
                #ym = m*xm + c

        #if disc >= 0. :
            #dp2 = dm2 = 1.e6
            #if corner['min_x'] <= xp <= corner['max_x'] and corner['min_y'] <= yp <= corner['max_y'] :
                #dp2 = (xp - self.xstart)**2 + (yp- self.ystart)**2

            #if corner['min_x'] <= xm <= corner['max_x'] and corner['min_y'] <= ym <= corner['max_y'] :
                #dm2 = (xm - self.xstart)**2 + (ym- self.ystart)**2

            #if dp2 < dm2 :
                ## make sure the intersection pointn is actually on the trajectory segment
                #if self.distancetopoint(xp, yp) < 1.e-6 :
                    #dst = sqrt(dp2)
                    #intercept_point = (xp, yp)
            #else :
                #if self.distancetopoint(xm, ym) < 1.e-6 :
                    #dst = sqrt(dm2)
                    #intercept_point = (xm, ym)

        #collide = dst < min_distance_to_intercept
        #if not collide:
            #print intercept_point
            #collide = collide

        #return collide

    #def constraintCollide(self, constraint):
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

#path = LineSegment(1.0, -1.0, 1.0, -3.0)
#wall = LineSegment(0.1, -0.1, 0.1, -2.1) # F parallel
#wall = LineSegment(0.5, -0.5, 2.0, -0.5) # F perpendicular
#wall = LineSegment(1.0, 0.0, 0.0, -2.0) # T same end point
#wall = LineSegment(0.0, -1.0, 1.0, 0.0) # T hit mid point
#wall = LineSegment(1.0, -1.0, -1.0, -1.0) # T cross over
#wall = LineSegment(0.0, -1.0, 0.0, -3.0) # T partial overlap
#wall = LineSegment(0.0, -0.5, 0.0, -1.0) # T subsection overlap of path
#wall = LineSegment(0.0, 1.0, 0.0, -3.0) # T superset overlap of path

#path = LineSegment(1.0, -1.0, 1.0, -3.0)
#corner = CircleSegment(1.0, -0.5, .26) # F inline above
#corner = CircleSegment(1.1, -1.0, .26) # T starting point inside circle
#corner = CircleSegment(0.9, -2.9, .26) # T end point inside circle
#corner = CircleSegment(1.2, -2.0, .26) # T point on right of line
#corner = CircleSegment(0.8, -2.0, .26) # T point on left of line


path = LineSegment(1.0, -1.0, 3.0, -3.0)
corner = CircleSegment(0.5, -0.5, .26) # F inline above
corner = CircleSegment(1.1, -1.1, .26) # T starting point inside circle
corner = CircleSegment(2.9, -3.1, .26) # T end point inside circle
corner = CircleSegment(2.0, -1.9, .26) # T point above line
corner = CircleSegment(2.0, -2.1, .26) # T point below line



#if path.collideswithsegment(wall):
    #print 'collide'
#else:
    #print 'no problem'


if path.collideswithcircle(corner):
    print 'collide'
else:
    print 'no problem'
