

import datetime
today=datetime.datetime.now()
print (today)
d1=datetime.date(2022,12,21)
y1=today.year
m1=today.month
day1=today.day
d2=datetime.date(y1,m1,day1)
dif1=abs((d2-d1).days)
print (dif1)
