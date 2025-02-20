# understanding of range
# my_range = range(7)
# print(type(my_range)) 
# print(my_range)
# print(list(my_range))
# print(tuple(my_range))
# print(set(my_range))

# my_range = range(10, 20, 3)
# print(type(my_range))
# print(my_range)
# print(list(my_range))

# # understanding of index in range
# my_range = range(10, 20, 3)
# print(my_range[0])
# print(my_range[1])
# print(my_range[2])
# print(my_range[3])
# print(my_range[4])

# my_range = range(5)
# print(my_range)
# print(type(my_range))
# print(my_range[-1])

# range mojno sozdavat i bez peremennoy
# for n in range(5):
#     print(n)

# for n in range(12,25,5):
#     print(n)
    
# print(list(range(12,25,5)))
# print(tuple(range(12,25,5)))
# print(set(range(12,25,5)))

# my_range = range(10,30,3)
# print(my_range.start) # eto attributy .start, .stop .step
# print(my_range.stop)
# print(my_range.step)


# my_range = range(10,30,3)
# # print(my_range.count(3))
# print(my_range.index(10))

# Conclusion of list, tuple, dict, set, range
# sravnenie tipov 
# list = izmenaymyy, i vajen poryadok, est index, odinakovye elementy
# tuple(kartej) = ne izmeniymye, vajen poryadok, est index, odinakovye elementy
# set(nabor) = izmenyaemyy, poryadok ne vajen, nelzya dobavlyat odinakovye elementy
# range = izmenyat nelzya, poryadok vajen, nemojet byt odinakovyh elementov
# dict = mojno izmenayt, poryadok ne vajen, 
# str(string) = ne izmenyaemye, vajen poryadok, est index, mogut byt odinakovye simvoly
# eto vse tipy posledovatelnosti
