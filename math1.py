import math

# print(math.pi)
# print(math.e)

# print(math.sqrt(25))

# print(math.log(100))

# print(math.factorial(10))

# print(dir(math))

def calc_factorial(num):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    if num <= 0:
        raise ValueError("Number must be positive")
    
    if num == 1:
        return 1
    return calc_factorial(num - 1) * num
    
print(calc_factorial(10))
print(math.factorial(10))


    