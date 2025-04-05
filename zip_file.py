from zipfile import ZipFile 

from pathlib import Path 

# Path('my_files').mkdir() # sozdanie papki

# with open('my_files/first.txt', 'w') as my_file: # sozdanie faila v papke
#     my_file.write('This is the first file')
    
# with open('my_files/second.txt', 'w') as my_file: # sozdanie ftorogo faila v papke
#     my_file.write('This is the second file')

with ZipFile('my_files.zip', mode='w') as my_zip_file:
    print('my_zip_file')

    
