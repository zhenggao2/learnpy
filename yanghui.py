# -*- encoding: utf-8 -*-
def yh_tri():
   n = 1
   L = []
   while n > 0:
       if n == 1:
           L.append([1])
       if n == 2:
           L.append([1, 1])
       if n > 2:
           t = []
           t.append(1)
           i = 0;
           while i < len(L[-1])-1:
               t.append(L[-1][i] + L[-1][i+1])
               i += 1
           t.append(1)
           L.append(t)
       yield(L[-1])
       n += 1
