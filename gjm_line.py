# gjm_Line.py

import math
from collections import namedtuple

Point = namedtuple("Point", "x y")
LineParms = namedtuple("LineParms", "m yi xi")


def _get_params(p1,p2):
    """
    Given two points p1,p2, find three parms: m,yi,xi and return them as a tuple.
    m=slope,yi=y-intercept or b, and xi=x-intercept for translation 
    """
    m = (p2.y-p1.y)/(p2.x-p1.x)
    # (y -p1.y)= m(x=p1.x)=> y = p1.y + m(x-p1.x) => b =y(x=0)= p1.y + m(0 - p1.x)
    # b= p1.y - m* p1.x and x-intercept, xi = x(y=0)=y - p1.y= m(x - p1.y)
    # x(y=0) =>(0-p1.y)/m +p1.x  => x(y=0) = -p1.y/m +p1.x  
    yi = p1.y - m* p1.x
    xi = -p1.y/m + p1.x
    return LineParms(m,yi,xi)



def _get_y(myixi, x ):
    """
    given the tuple myixi = (m,iy,ix) where m=slope,yi= y-intercept b,and xi=x-intercept, the shift value of x,
    Returns the value of y depending if translate: y=mx+yi else: y=m*(x+xi)+ yi.
    equation: y = mx +b 
    """
    y = myixi.m * x + myixi.yi
    return y 


def get_y_from_points(p1, p2, x):
    """
    Usage: User gets two points on a Line of an equation. He defines the Points as tuples p1=gl.Point(x1,y1) p2=gl.Point(x2,y2)
    Then He starts a python session : python3.9 and imports gjm_line.py as gl and from gjm_line import get_y_from_points
    Then he calls get_y_from_points(p1,p2, x ). The extrapolation or interpolation value of y  is returned.
    Given x and two points, Return y = f(x)
    parms is LineParms(m,yi,xi) where m=slope, yi=y_intercept xi=x_intercept
    """
    parms = _get_params(p1,p2)
    return _get_y(parms,x)
