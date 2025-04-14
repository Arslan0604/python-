import secrets
import string 

all_chars = string.ascii_letters + string.digits + string.punctuation

print(''.join(secrets.choice(all_chars) for i in range(15))) # vybor 

# print(string.ascii_letters) # all_letters
# print(string.ascii_lowercase) # lowecases 
# print(string.ascii_uppercase) # uppercases
# print(string.digits) # digits 
# print(string.punctuation) # simbols


# print(string.ascii_letters + string.digits + string.punctuation) # concat