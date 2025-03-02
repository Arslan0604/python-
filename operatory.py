arslan_1 = {10, 'abc', 50, True} # poryadok ne imeet znacheniya
arslan_2 = {10, 'abc', 50, True}

arslan_1 == arslan_2
print(arslan_1 == arslan_2) # True
print(arslan_1.__eq__(arslan_2)) 
print(arslan_1 in arslan_2)