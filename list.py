bicycles = ['trek', 'cannondale', 'redline']
print(bicycles)

print(bicycles[0])
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-2].title())

bicycles[1] = "test"
print(bicycles)

bicycles.append("hello")

print(bicycles)

# empty list
hi = []


bicycles.insert(0, "nihao")
print(bicycles)

del bicycles[0]
print(bicycles)

popdata = bicycles.pop()
print(bicycles)
print(popdata)

pop1 = bicycles.pop(1)
print(bicycles)
print(pop1)

bicycles.remove('trek')
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars))

print(cars)

print(sorted(cars, reverse=True))

print(cars)

cars.reverse()
print(cars)

l = len(cars)

print(l)

#print(cars[10])
#print(hi[-1])