
# def mult(a, b):
#     return a * b 

# mult = lambda a, b: a + b

# print(mult(10, 5))

def greeting(greet):
    return lambda name: f"{greet}, {name}"

morning = greeting("Good Morning")

print(morning("Arslan"))

evening = greeting("Good Evening")

print(evening("Arslan")) 



 
