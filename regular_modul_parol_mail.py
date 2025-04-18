# import re

# my_string = "My name is Arslan. Aoooon is enterpreneure"



# # res = re.search(r'A....n\.$', my_string)

# # print(res.span())
# # print(res.start())
# # print(res.end())

# my_pattern = re.compile(r'A....n')

# print(my_pattern)

# print(my_pattern.findall(my_string))

# proverka maila teper izuchim

# import re 
# def check_email(email):
#     email_regexp = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$" # pattern for mail
#     email_check_pattern = re.compile(email_regexp)
#     validation_result = "valid" if email_check_pattern.fullmatch(email) else "not valid"
#     return (email, validation_result)


# # Valid
# print(check_email('bs@gmail.com'))
# print(check_email('b_s@gmail.com'))
# print(check_email('b.s@sub.gmail.com'))
# print(check_email('bs@gmail.com'))
# # Invalid
# print(check_email('bs@gmailcom'))
# print(check_email('bs@.com'))
# print(check_email('bsgmail.com'))
# print(check_email('@gmail.com'))

# Task to solving

import re # vstrinyy modul

# vse chto kak nado delat parol 

def check_password(password):
    length_pattern = re.compile(r"\S{8,}") # opredelyaet dliny 
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$") # kak minimum malenkaya bukva 
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$") # kak minimum bolsya bukva
    number_pattern = re.compile(r"^.*[0-9]+.*$") # kak minimum cyfra
    spacial_symbol_pattern = re.compile(r"^.*[@#?!*^]+.*$") # spec znaki 
    no_whitespace_pattern = re.compile(r"^\S*$")   # proveryate probely
    
    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespaces allowed in the password")
        
    
    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at least 8 symbols")
    
    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase letter")
    
    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercase letter")
    
    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")
    
    if not re.fullmatch(spacial_symbol_pattern, password):
        return (False, "Password must have at least one symbol @#?!*^")
    
    
    return(True, "Password is valid!")

# print(check_password('1234ASD0980     as!@'))
# print(check_password('123'))
# print(check_password('12345678'))
# print(check_password('1234567a'))
# print(check_password('asdfASDFA'))
# print(check_password('1234sdLKJLJ'))
# print(check_password('1234ASDFasdf!@'))

while True:
    password = input("Please enter your password: ")
    password_check_result = check_password(password)
    if password_check_result[0]:
        print(password_check_result[1])
        break
    
    print(password_check_result[1])

    





