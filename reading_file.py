
# sozdanie zapisya v fail
with open('test.txt', 'w') as test_file:
    test_file.write('First string\n')
    test_file.write('Second string\n')
    test_file.write('Third string\n')
    
# chtenie iz faila
with open('test.txt') as test_file:
    lines = test_file.readlines()
    for line in lines:
        print(line)
    



