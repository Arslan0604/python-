from pathlib import Path 

files_dir = Path('files')
files_dir.mkdir(exist_ok=True)

first_file = files_dir/'first.txt'
second_file = files_dir/'second.txt'

with open (first_file, 'w') as f:
    f.write('First line \n')
    f.write('Second line \n')

with open (second_file, 'w') as f:
    lines = [
        "first line in second file",
        "second line in second file",
        "last line in the second file"
    ]
    for line in lines:
        f.write(line + '\n')
    
    
with open(first_file) as f: 
    print(f.read())
    
with open(second_file) as f:
    for line in f: # option 1
        print(line.strip())
        # option 2
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     print(line.strip())
        
        
        
first_file.unlink()
second_file.unlink()


files_dir.rmdir()
        
