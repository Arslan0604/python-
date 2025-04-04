from pathlib import Path 

files_dir_path = Path('files')
files_dir_path.mkdir(exist_ok=True)

with open (files_dir_path/'first.txt', 'w') as f:
    f.write('First line \n')
    f.write('Second line \n')

with open (files_dir_path/'second.txt', 'w') as f:
    lines = [
        "first line in second file",
        "second line in second file",
        "last line in the second file"
    ]
    for line in lines:
        f.write(line + '\n')
        