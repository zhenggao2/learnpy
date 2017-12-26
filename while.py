# -*- encoding: utf-8 -*-
n = 0
while n < 100:
    if n % 2 == 0:
        n += 1
        continue
    else:
        print(n)
        n += 1

