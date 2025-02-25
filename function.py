# def my_fn(a, b):
#     a = a + 1
#     c = a + b 
#     return c

# arslan = my_fn(10, 10 )
# print(arslan)

# def my_fn():
#     pass 

# print(my_fn())

# izmenyaemye obekty
# def increase_person_age(person):
#     print(id(person))
#     person['age'] += 1
#     return person
# person_one = {
#     'name' : 'Arsalan',
#     'age' : 42
# }
# print(id(person_one))
# increase_person_age(person_one) 
# print(person_one['age'])

# sozdanie copy
# def increase_person_age(person):
#     person_copy = person.copy()
#     person_copy['age'] += 1
#     return person_copy

# person_one = {
#     'name' : 'Arsalan',
#     'age' : 42
# }

# new_person = increase_person_age(person_one)
# print(new_person['age'])
# print(person_one['age'])

# def merge_lists_to_dict(list1, list2):
#     dict1 = dict(zip(list1, list2))
#     return dict1

# list1 = ['name', 'age', 'city']
# list2 = ['Arslan', 42, 'Ashgabat']

# print(merge_lists_to_dict(list1, list2))    

def merge_lists_to_dict(list1, list2):
    zipped_seq = zip(list1, list2)
    return dict(zipped_seq)

res_one = merge_lists_to_dict(['a', 'b', 'c'], [10, True, []])
print(res_one)

res_two = merge_lists_to_dict(['abc'], [{}, True, 100])
print(res_two) 

res_tree = merge_lists_to_dict([10, True, 100], ['abc', 'jango', 'mango'])
print(res_tree)


