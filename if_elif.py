# my_number = 24

# if my_number > 0:
#     print(my_number, "is positive number")

# num_one = 10 
# num_two  = 5.2

# if (num_one > 0 and 
#     num_two > 0 and 
#     isinstance(num_one, int) and 
#     isinstance(num_two, float)):
    
#     print("Both numbers are ints and positive")


# my_phone = {
#     'price' : 200,
    
# }
# print(my_phone.get('brand'))
# print(bool(my_phone.get('brand')))
      
# if my_phone.get('brand'):
#     print("Phone's brand is", my_phone['brand'])
# else:
#     print("There is no phone brand")

# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "One of them is not int"
    
#     if a >= b:
#         return f"{a} more or equel {b}"
    
#     return f"{a} less {b}"

# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         info = "One of them is not int"
#     elif a >=b:
#         info = f"{a} more or equel {b}"
#     else:
#         info = f"{a} less {b}"
        
#     return info

# print((nums_info(True, 10)))
# print(nums_info(10, 2))
# print(nums_info(4, 15))

# tasks 

def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your distanation is {route['distance']}"
    
    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * 
        route['time']}"
        
    return "No distance info is available"
    
print(route_info({'distance': 14}))
# Distance to your distanation is 14
print(route_info({'speed' : 45, 'time' : 4}))
# Distance to your destination is 180
print(route_info({'my_speed': 45}))
# No distance info is available


    

    