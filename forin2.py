# all_nums = [-3, 1, 0, 10, -20, 5]

# absolute_nums = []

# for num in all_nums:
#     absolute_nums.append(abs(num))
    
# print(absolute_nums)

# print(all_nums)

# drugoy sposob 
# all_nums = [-3, 1, 0, 10, -20, 5]
# absolute_nums = [abs(num) for num in all_nums]
# print(absolute_nums)
# print(all_nums)

# drugoy primer

# all_nums = [-3, 1, 0, 10, -20, 5]
# positive_nums = []
# for num in all_nums:
#     if num > 0:
#         positive_nums.append(num)
        
# print(positive_nums)
# print(all_nums)

# drugoy sposob 
# all_nums = [-3, 1, 0, 10, -20, 5]
# positive_nums = [num for num in all_nums if num > 0]
# print(positive_nums)
# print(all_nums)

# primer s set
# my_set  = {1, 10, 15}
# new_set = {val * val for val in my_set}
# print(new_set)
# print(my_set)

# drugoy promer s dict 
# my_scores = {
#     'a' : 10,
#     'b' : 7,
#     'm' : 14
# }
# scores = {}

# for key, value in my_scores.items():
#     scores[key] = value * 10
    
# print(scores)
# print(my_scores)

# sokrashennyy sposob 
# is spiska formirovanie slovarya 
# my_scores = [10, 7, 14]

# my_scores = {
#     '0' : 10,
#     '1' : 7,
#     '2' : 14
# }
# scores = {k: v for k, v in enumerate(my_scores)}

# print(type(scores))
# print(scores)
# print(my_scores)

# task 1 

# my_nums = {
#     'brand': 'arslan',
#     'country': 'dog',
#     'owner': 'ml'
# }
# znachenie = {k: v.upper() for k, v in my_nums.items()}

# print(znachenie)
# print(my_nums)

# task 2

# my_list = ['arslan', 'dog', 'ar']

# jango = [el for el in my_list if len(el) > 3]

# print(jango)
# print(my_list)

# generatory v for in 
from sys import getsizeof

squares_gen = (num * num for num in range(100_000_000))
print(getsizeof(squares_gen))

print(type(squares_gen))

for elem in squares_gen:
    print(elem)
    if elem == 100:
        break

squares_list = [num * num for num in range(100_000_000)]
print(getsizeof(squares_list))

print(type(squares_list))


