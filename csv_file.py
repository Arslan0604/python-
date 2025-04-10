import csv 

# with open('test.csv', 'w') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerow(['user_id', 'user_name', 'comments_qty'])
#    writer.writerow([234, 'Arslan', 3])
#    writer.writerow([231, 'Serdar', 4])
#    writer.writerow([343, 'Jambul', 5])
    
# with open('test.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for line in reader:
#         print(line)
        
#     for line in reader:
#         print(line)
        
#     print(reader.line_num)

# teper menyaem delimiter na ; 
    
with open('test.csv', 'w') as csvfile:
   writer = csv.writer(csvfile, delimiter=';')
   writer.writerow(['user_id', 'user_name', 'comments_qty'])
   writer.writerow([234, 'Arslan', 3])
   writer.writerow([231, 'Serdar', 4])
   writer.writerow([343, 'Jambul', 5])
   
with open('test.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for line in reader:
        print(line)
        
    for line in reader:
        print(line)
    print(reader.line_num) #  on potom peresapisyvaetsya
