def decorator_function(original_fn):
    def wrappper_function(*args, **kwargs):
        # some actions before execution of the original_fn
        print("Executed before function")
        
        result = original_fn(*args, **kwargs)
        
        print("Function result:", result)
        
        # some actions after execution of the original_fn
        print("Executed after function")
        
        return result

    return wrappper_function

@decorator_function
def my_function(a, b):
    print("this is my function!")
    return (a, b)
    
result = my_function(100, 40)
print(result)