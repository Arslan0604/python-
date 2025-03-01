# def print_number_info(num):
#     """
#     Prints num information

#     Args:
#         num (int): Integer number

#     Returns:
#         int: Same number
#     """
#     if (num % 2) == 0: 
#         print("Num is even")
#     else:
#         print("Num is odd")
        
        
#     return num 
        
        
# print_number_info()

# oblasti vidimosti peremennih

# a = 10 

# def my_fn():
#     a = True
#     b = 15
#     print(a)
#     print(b)
    
# my_fn()

# print(a)
# print(b) # here gives a mistake 


# ispolzovanie global peremennih
# a = 10 
# def my_fn():
#     global a 
#     a = 45
# my_fn()
# print(a)


c = 5
def my_fn(a, b):
    print(c)
    print(a,b)
    print(dir())
    
my_fn(4, 5)
    


