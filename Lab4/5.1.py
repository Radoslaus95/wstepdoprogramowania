values = [10,20,30]
keys =["dziesięć","dwadzieścia","trzydzieści"]
# d1 = dict(zip(keys,values))
# print(d1)
d1 = {}
for i in range(3):
    d1[keys[i]] = values[i]
print(d1)

d2 = dict(trzydzieści = 30,czterdzieści = 40,piędziesiąt = 50)
print(d2)
d3 = d1.copy()
print(d3)
d3.update(d2)
print(d3)