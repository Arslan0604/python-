# this list for loop
# my_list = [True, 10, 'abc', {}] 
# for elem in my_list:
#     print(elem)

# this for tuple(carteje)
# video_info = ('1920x1080', True, 27)
# for elem in video_info:
#     print(elem)

# for in for dictioneries 
# my_object = {
#     'x': 10,
#     'y': True,
#     'z': 'abc'
# }
# for key in my_object:
#     print(key, my_object[key])

# my_dict = {'id': 432, 'title': 'test'}
# for key in my_dict:
#     print(type(key))
#     print(key)
#     print(my_dict[key])

# iteraciya 
# my_dict = {'id': 233, 'title': 'test'}
# for item in my_dict.items():
#     k, v = item    # raspokovka posledovatelnosti
#     print(k, v)

# set(nabor) eto ne uporadochnye posledovatelnosti 
# video_ids = {132,323,434,453,2323}
# for id in video_ids:
#     print(id)

# for in dlya strok
# my_name = 'Arslan'
# for char in my_name:
#     print(char)

# for in for range(diapozonov)
# for num in range(5):
#     print(num)
# for odd_num in range(3, 10, 2):
#     print(odd_num)

# task 1 
# def dict_to_list(dict_to_convert):
#     list_for_convertion = []
#     for k, v in dict_to_convert.items():
#         if type(v) == int:
#             v *= 2
#         list_for_convertion.append((k, v))
#     return list_for_convertion
    
# print(dict_to_list({'a': 10, 'b': [], 'c': 23}))
# tast 2
# def filter_list(list_to_filter, value_type):
#     filtered_list = []
#     for element in list_to_filter:
#         if type(element) == value_type:
#             filtered_list.append(element)
#             ## Not recommended, because bool is subclass of int
#         # if isinstance(element, value_type):
#         #     filtered_list.append(element)
#     return filtered_list

# print(filter_list([32, True, 'ads', 10], int))
# print(filter_list([32, True, 'ads', 10], str))
# print(filter_list([32, True, 'ads', 10], bool))


   
def filter_list(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, 
                       list_to_filter))

res = filter_list([1, 33, 'abc',True, 4.3], int)
print(res)
    
    
