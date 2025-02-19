# dublikaty udalayutsya avtomaticheski v setah 
# indexov u setov net potomu chto ne uporadochna nabor
# eslit net magicheskogo getitem
# v setah tolko unikalnye elementy ne mogut byt izmenyaemye elementy
# set ne podderjivaet operator del, vy nemojete udalit
# tuple(karteji) normalno s nimi set rabotaet potomu chto oni toje ne izmenyaemye
# v setah ne mogut prisustvyvat izmenyaemye nabory
# posts_ids = {43, 23, 13, 56, 23}
# print(posts_ids)
# lists_set = {[1,3], [20,5]}
# print(lists_set)
# my_set = set()
# print(my_set)
# print(type(my_set))
# metody nabory seychas rasmotrim
# metod .add dobavlyaet novyy element priment nije 
# photo_sizes = {'2323*2', '5454/2'}
# photo_sizes.add('54*54')
# print(photo_sizes)
# sleduyushiy nabor Union obedinenie naborov 
# photo_sizes = {'434*43', '56*34'}
# other_sizes = {'56*34', '343*34'}

# all_sizes = photo_sizes.union(other_sizes)
# print(all_sizes)
# sleduyushiy metod intersection kotoryy opredelyaet dublicaty
# photo_s = {'434*43', '56*34'}
# other_s = {'56*34', '343*34'}

# common_s = photo_s.intersection(other_s)

# print(common_s)
# the next method is ISSUBSET checking vkluchen li odin nabor v drugoy 
# nums = {10, 5, 35}
# other_nums = {20, 5, 12, 10, 35}

# res = nums.issubset(other_nums)
# print(res)

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))











