# -*- encoding: utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print('%s(%d) --> %s(%d)' % (a, n, c, n))
        return

    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)
