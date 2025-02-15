#1
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print(current_date.strftime("%Y-%m-%d"))
print(new_date.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("yesterday: ", yesterday.strftime("%Y-%m-%d"))
print("today: ", today.strftime("%Y-%m-%d"))
print("tomorrow: ", tomorrow.strftime("%Y-%m-%d"))

#3
from datetime import datetime

today = datetime.now()
new_time = today.replace(microsecond=0)
print(new_time)

#4
from datetime import datetime

date1 = input("(YYYY-MM-DD HH:MM:SS)")
date2 = input("(YYYY-MM-DD HH:MM:SS)")

date11 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
date22 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

different = int(abs((date11 - date22).total_seconds()))
print("difference:", different)
