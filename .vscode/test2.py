"""import numpy as np

d = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],
              [[11, 12, 13, 14],
               [15, 16, 17, 18],
               [19, 20, 21, 22]]])
print(d.ndim)
print(d.shape)
a=str(d)

d=np.array(a)

print(d)
print(d.ndim)
print(d.shape)"""
import numpy as np
d = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],
              [[11, 12, 13, 14],
               [15, 16, 17, 18],
               [19, 20, 21, 22]]])
print(d.ndim)
print(d.shape)
a=d.tolist()
a=str(a)


characters = "[],"
for x in range(len(characters)):
    a = a.replace(characters[x],"")
print(a)

a=a.split()
a=list(map(int,a))
d=np.array(a).reshape((2,3,4))
print(d)
print(type(d))
print(d.ndim)
print(d.shape)