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

test_password = 'ABASasd!3432423'

def check_password(password):
    length_pattern = re.compile(r"\S{8,}") 
    lowercase_pattern = re.compile(r"[a-z]+")
    uppercase_pattern = re.compile(r"[A-Z]+")
    number_pattern = re.compile(r"[0-9]+")
    spacial_symbol_pattern = re.compile(r"[@#?!*^]+")
    
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
    
    
print(check_password(test_password))
    





