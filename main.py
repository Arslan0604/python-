my_cars = ['BMW', 'Mercedes', 'Audi', 'Toyota', 'Honda']

copied_cars = my_cars 
copied_cars.append('Ford')

print(copied_cars)

print(my_cars)

print(id(my_cars) == id(copied_cars))

copied_cars = my_cars[:]

copied_cars.append('Chevrolet')

print(copied_cars)
print(my_cars)

print(id(my_cars) == id(copied_cars))





 