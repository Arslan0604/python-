# from datetime import date
# my_date  = date(2100, 4, 13)
# print(my_date)
# print(my_date.isocalendar())

# from datetime import time
# my_time = time(15, 54, 32)
# print(my_time)
# print(my_time.hour)
# print(my_time.minute)
# print(my_time.second)

from datetime import datetime, timedelta
my_datetime = datetime(2102, 12, 13, 12, 59, 12, 2133)
# print(my_datetime)
# print(my_datetime.year)
# print(my_datetime.hour)
# print(my_datetime.second)
# print(my_datetime.now().microsecond)

# print(my_datetime.strftime('%d-%b-%Y')) # 3-Dec-2102
# print(my_datetime.strftime('%d-%b-%Y %H:%M:%S' )) # 13-Dec-2102 12:59:12

# date_str = '10/12/2222'

# converted_date = datetime.strptime(date_str, '%d/%m/%Y')

# print(converted_date)

print(my_datetime + timedelta(days=100, minutes=120, hours=2)) # ty mojesh i minusovat toje 