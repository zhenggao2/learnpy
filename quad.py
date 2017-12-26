# -*- encoding: utf-8 -*-
from math import sqrt
def quad(a, b, c):
    if a == 0:
        if b == 0:
            print('no solution')
            return
        else:
            x1 = -c/b
            return x1

    delta = b*b-4*a*c
    t = -b/(2*a)
    if delta < 0:
        delta = abs(delta)
        x1 = '(%.2f, %.2f)' % (t, sqrt(delta)/(2*a))
        x2 = '(%.2f, %.2f)' % (t, -sqrt(delta)/(2*a))
    elif delta == 0:
        x1 = t
        x2 = -t
    else:
        x1 = t + sqrt(delta)/(2*a)
        x2 = t - sqrt(delta)/(2*a)
    return x1,x2
