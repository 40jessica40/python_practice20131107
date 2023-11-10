#datetime模块是Python标准库中用于处理日期和时间的模块，它提供了多种类和函数，用于处理日期，时间，时间间隔等操作。


#6.1、获取当前日期时间
import datetime
# current_time = datetime.datetime.now()


#6.2、格式化当前日期时间
import datetime
current_time = datetime.datetime.now()
r = current_time.strftime('%Y-%m-%d %H-%M-%S')
print(r)



#6.3、解析日期时间
import datetime
date = '2023-03-29 10:30:33'
cdt = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
print(cdt,type(cdt))

#6.4、计算日期间隔 使用timedelta类可以进行日期间隔的计算
import datetime
from datetime import timedelta
date1 = datetime.datetime(2023,3,29)
date2 = datetime.datetime(2023,11,20)
date_diff = date2 - date1
print('Date Difference is:',date_diff)
work_time = date1 + timedelta(days=208)
print('work date is:',work_time)

#6.5、比较日期 可以直接比较datetime对象来判断日期的先后关系
import datetime
date1 = datetime.datetime(2023, 10, 12)
date2 = datetime.datetime(2023, 10, 12)
if date1>date2:
    print("date1大于date2")
elif date1<date2:
    print("date1小于于date2")
else:
    print("date1等于date2")




#6.6、获取日期和时间的部分信息
import datetime
current_time = datetime.datetime.now()
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

