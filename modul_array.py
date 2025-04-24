from array import array


my_int_array = array('i',[5, 5, 3,4,6,7])

with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)

imported_array = array('i')

with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 4)
    print(imported_array)

imported_array.reverse()
print(imported_array)