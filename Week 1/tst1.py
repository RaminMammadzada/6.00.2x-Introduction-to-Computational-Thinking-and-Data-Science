import random
d1 = {}
for i in range(10000):
    x = random.randrange(10)
    print str(x)
    d1[x] = d1.get(x, 0) + 1
d2 = {}
for i in range(10000):
    x = int(random.random()*10)
    d2[x] = d2.get(x, 0) + 1
d3 = {}
for i in range(10000):
    x = random.randint(0, 10)
    d3[x] = d3.get(x, 0) + 1
