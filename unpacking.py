# my_fruits = ['apple', 'banana', 'cherry']

# # #raspokovka spiska v python
# arslan, batyr, guncha = my_fruits

# # my_apple = my_fruits[0]
# # my_banana = my_fruits[1]    
# # my_cherry = my_fruits[2]

# print(arslan)
# print(batyr)
# print(guncha)

# my_list = [1,2,3]

# first, second, third = my_list

# print(first)
# print(second)
# print(third)

# pri tuple toje samoe tolko dobavlyat nichto ne vozmojno i v kobkah 

# ispolzovat * operator dlya raspakovki spiska
# my_fruits = ['apple', 'banana', 'cherry']

# my_apple, *remaing_fruits  = my_fruits

# print(my_apple)
# print(remaing_fruits)
# print(type(remaing_fruits))

# raspokovka slovarya s keys

# user_profile = {
#     'name': 'Arslan',
#     'comments_gty': 100,
# }

# def user_info(name, comments_gty=0):
#     if not comments_gty:
#         return f"User {name} has no comments"
    
#     return f"User {name} has {comments_gty} comments"

# # print(user_info(user_profile['name'], user_profile['comments_gty']))
# # another version to do that 
# print(user_info(**user_profile))

# # raspokovka spiska v pozicionnom argumente
# user_data = ['Arslan', 43]

# def user_info(name, comments_gty):
#     if not comments_gty:
#         return f"{name} has no comments"
    
#     return f"{name} has {comments_gty} comments"


# print(user_info(*user_data))

# esli ispolzovat ** to doljno by para kluch znacheniye

# neudavshiysya primer dlya menay
# arslan_name = {'arslan': 'great', 
#                'money': 1000000, 
#                'education': True}

# def arslan_info(feeling, earing, bool):
#     if not earing: 
#         return f"You are earned under {earing}"
#     return f"You are {feeling} person, and earing is {bool}"

# feeling, earing, bool = arslan_name

# print(arslan_info(feeling, earing, bool))
