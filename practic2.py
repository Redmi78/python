v=[1,2,3,5,4,1]
print(v)
print(v[-2])
print(v[0:4:2])
print(v.pop(1))
print(v)

a=(1,2,3,2,5)
b=(1,2,3,3,5)
print(a)
print(min(a))
print(max(a))
print(a is b)


c={1:"apple",2:"banana",3:"cherry"}
print(c)
print(c[1])
c.update({4:"orange"})
print(c)
c.pop(2)
print(c)


for i in c.keys():
    print(i)

for i in c.values():
    print(i)


