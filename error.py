#  Obrabotka errors

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(type(e))
#     # print(dir(e))
#     print(e)
    
# print("Program continues")

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else: 
#     print("There was not error")
# finally:    
#     print("Program continues")

# we need to create mistakes 

# def divide_nums(a, b):
#     if b == 0:
#         raise TypeError("Second number can't be zero")
#     return a / b

# print(divide_nums(10, 0))

# task 1
def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Keys image_id and image_title must be present")
    return f"Image '{img['image_title']}' has id {img["image_id"]}"

print(image_info({'image_title': 'My jango', 'image_id': 43}))
# obrabotka oshibki
try:
    
    print(image_info({'image_title': 'My jango'}))
except TypeError as e:
    print(e)        
    
    