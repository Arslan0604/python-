# # grey_button = {
# #     'width': 200,
# #     'text': 'Buy',
# #     'color': 'grey',
# # }

# # red_button = {
# #     'color': 'red',
# #     **grey_button,
# # }

# # print(red_button) 
# # print(grey_button)

# button_default = {
#     'text': 'ok',
#     'color': 'black',
#     'width': 0,
#     'height': 0
# }

# button_style = {
#     'color': 'yellow',
#     'width': 200,
#     'height': 300
# }

# # button = {
# #     **button_info,
# #     **button_style
# # }
# # or  
# button = button_default | button_style 

# print(button)

arslan_1 = {
    'name': 'arsicola',
    'color': 'blue',
    'kg': 100,
    
}
arslan_2 = {
    'monstr': 'mustang',
    'color': 'black',
    'kg': 50,
    
}
arslan_3 = {
    'jango': 'arsicola',
    'color': 'blue',
    'kg': 85,
    
}

arslan_best = arslan_1 | arslan_2 | arslan_3

print(arslan_best)
