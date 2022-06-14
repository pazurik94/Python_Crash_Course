motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('ducati')
print(motorcycles2)

motorcycles3 = ['honda', 'yamaha', 'suzuki']
motorcycles3.insert(0, 'ducati')
print(motorcycles3)

print(motorcycles)
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles2.pop(1)
print(f"The first motorcycle I owned was a {first_owned.title()}")

too_expensive = "ducati"
print(motorcycles3)
motorcycles3.remove(too_expensive)
print(motorcycles3)
print(f"A {too_expensive.title()} is too expensive for me.")