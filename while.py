# simple explanition of while loop
# i = 10

# while i < 50: 
#     print(i)
#     i += 10 

# while True:
#     answer = input('Enter yes or no: ')
#     if answer == 'no':
#         break
    
# import random

# random_num = random.randint(1, 5)
# while True:
#     num = int(input('Guess the number from 1 to 5: '))
#     if num != random_num: 
#         print('Try again...')
#         continue
#     print('Congratulations!', random_num)
#     break

# task 

while True:
    try: 
        num_one = float(input("please enter number one: "))
        num_two = float(input("please enter number two: "))
    except ValueError as e:
        print(e)
        print("you must enter numbers")
        continue
        
    print(num_one / num_two)
    
    answer = input("do you want to continue? (yes/no): ")
    if answer == 'no':
        break