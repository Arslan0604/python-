# from os import path

# print(path.abspath('.'))
# from pathlib import Path 


# my_dir = Path('/Users')/'macbookpro'/'Desktop'/'Python'/'django'

# if not my_dir.exists():  # dobavlyaet papku
#     my_dir.mkdir()
    
    
# if my_dir.exists():      # udalyaet papku 
#     my_dir.rmdir()


# from pathlib import Path

# print(type(Path('.')))

# from pathlib import Path

# cwd = Path('.')

# print(isinstance(cwd, Path))  # True
# print(type(cwd))

from pathlib import Path
# file_path = Path('test.txt')

# print ([m for m in dir(file_path) if not m.startswith('_')]) 

# print(Path.cwd())  # your directory 

# print(Path('usr').joinpath('local').joinpath('bin'))
# # or 
# print(Path('urs') / 'local' / 'bin')

# print(Path('main.py').exists())  # True

# print(Path('/Users/macbookpro/Desktop').exists())  # True

# print(Path('other.py').exists())  # False

# print(Path('main.py').is_file())  # True
# print(Path('../python').is_file())  # False
# print(Path('../python').is_dir()) # False

# for f in Path('.').iterdir():
#     print(f)
    

# from os import path

# print(path.abspath('.'))


from pathlib import Path



cwd = Path('.')

print(isinstance(cwd, Path))
print(type(cwd))

print(Path.__subclasses__())