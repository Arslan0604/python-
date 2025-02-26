# def ars_done(a, b):
#     asr = a * b 
#     return asr

# print(ars_done(100, 34))

# def sum_nums(*args):
#     print(args)
#     print(type(args))
#     # print(args[0])
#     return sum(args)
# print(sum_nums())

# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} books and his is real men"
#     return info
# info = get_posts_info( posts_qty=45, name='Arslan')
# print(info)

#obedinenie v slovar **
# def get_posts_info(**person):
#     print(person)
#     print(type(person)) 
#     info = (
#         f"{person['name']} wrote "
#         f"{person['posts_qty']} great books"
#     )
#     return info
# info = get_posts_info(name='Arslan', posts_qty=45, id = 43 )
# print(info)

# zadacha 1 

# def merge_lists_to_dict(list1, list2):
#     zipped_seq = zip(list1, list2)
#     return dict(zipped_seq)

# res_one = merge_lists_to_dict(list1=['a', 'b', 'c'],list2=[10, True, []])
# print(res_one)

# res_two = merge_lists_to_dict(['a', 'b', 'c'],list2=[10, True, []])
# print(res_two)

# zadacha 2
def update_car_info(**car):
    car['is_available'] = True
    return car

print(update_car_info(brand='Toyota', price=34343))

#TypeError: update_car_info() takes 0 positional arguments but 2 were given
# print(update_car_info('Toyota', 34343))





