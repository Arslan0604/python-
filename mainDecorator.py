# def log_function_call(fn):
#     def wrapper(*args, **kwargs):
#         print(f"Function name: {fn.__name__}")
#         print(f"Function arguments: {args}, {kwargs}")
#         result = fn(*args, **kwargs)
#         print(f"Function result: {result}")
#         return result
    
#     return wrapper
# @log_function_call
# def mult(a, b):
#     return a * b

# print(mult(5, 2))

# print("")

# @log_function_call
# def sum(a, b):
#     return a + b

# print(sum(a = 40.3, b = 40.5))

# now another primer eto otdelno ot verhnego 

def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            
                if not isinstance(arg, int) and not isinstance(arg, float):
                    raise ValueError(f"Type of the {arg} is {type(arg)}",
                                     "All arguments must be int or float")
            
        result = fn(*args, **kwargs)
        return result
    
    return wrapper
@validate_args
def sum_nums(a, b):
    return a + b

try: 
    print(sum_nums(7, 2))
    print(sum_nums(10.5, 2.3))
    print(sum_nums(a=10.5, b="2.0"))
except ValueError as e: 
    print(e)       

    