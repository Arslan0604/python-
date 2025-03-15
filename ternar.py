my_img = ('1920', '1080')

# info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else "Incorrect image formatting"

if len(my_img) == 2:
    info = f"{my_img[0]}x{my_img[1]}"
else:
    info = "Incorrect image formatting"
    
print(info)

my_str = "Very, very, very, very, very,very, very,very, very,very, very,very, very,very, very,very, very,very, very,very, very,very, very,very, very,very, very,"

print("String is long" if len(my_str) > 79 else "String is short")
 


