
# import json 
# json eto prosto stroka nenado zabyvat
# json_str = '{"id": 235, "brand": "Nike", "qty":84, "status": {"isForSale": true}}'

# json_array = '[{"a": 1}, {"b": 2}]' # massim object 


# sneakers = json.loads(json_str)

# print(type(sneakers))
# print(sneakers)

# # print(sneakers['brand'])
# # print(sneakers['qty'])
# # print(sneakers['status']['isForSale'])

# # method json.dumps perevodit list ili massiv v json format dlya otpravki na server

# my_list = json.loads(json_array)

# print(my_list)

# import json

# json_str = '{"id": 235, "brand": "Nike", "qty":84, "status": {"isForSale": true}}'

# sneakers = json.loads(json_str)

# json_from_dict = json.dumps(sneakers, indent=2)  # zagrujaem na server v takom vide

# print(json_from_dict)

# print(type(json_from_dict))

# task 1 this is my solution 
# import json

# json_task = '{"arslan": "great", "age": 43, "hobbies": true}'

# jonny = json.loads(json_task)

# print(type(jonny))
# print(jonny)

# task 2 this is yours solution
import json

my_dict = {
    'a': 10,
    'b': {
        'c': [1,2,3]
    },
    'd':(1,2,3,)
}

converted_dict = json.dumps(my_dict, indent=2) # conver to json process

print(converted_dict)
print(type(converted_dict))

# teper obratno v slovar convernut nado 

converted_dict = json.loads(converted_dict)
print(converted_dict)
print(type(converted_dict))