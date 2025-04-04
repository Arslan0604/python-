from pathlib import Path 

file  = open('test.txt', 'w')
file.close()

my_file = Path('test.txt')
if my_file.exists():# проверяет существует ли файл
    my_file.unlink() # удаляет файл

    

    



