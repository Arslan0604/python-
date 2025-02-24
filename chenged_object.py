# my_number = 10
# print(id(my_number))

# other_number = 10 
# print(id(other_number))

# print(id(other_number))


# adressa izmenayemye object

# my_list = [1,2,3]
# other_list = [1,2,3]
# other_list.append(4)
# print(my_list)
# print(other_list)


from copy import deepcopy

info = {
    'name' : 'Arslan',
    'is_greate' : True,
    'reviews' : []
}

info_shallow_copy = info.copy()
info_shallow_copy['reviews'].append('Great course')
info_shallow_copy['reviews'].append('What are you')

info['new_key'] = 50

print(info)

print(info_shallow_copy)