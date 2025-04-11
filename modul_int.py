import random

print(random.random())

print(random.randint(1, 10))
print(random.choice('abcd'))

print(random.choice([1,10,4]))

print(random.choices([1,10,4, 43, 44], k = 2))
