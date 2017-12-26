from yanghui import yh_tri

L = []
n = 0
for i in yh_tri():
    L.append(i)
    n += 1
    if n > 10:
        break
print(L)
