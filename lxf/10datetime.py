# datetime 是 Python 处理时间和日期的标准库

# 1. 获取当前日期和时间
from datetime import datetime

now = datetime.now()
print(now)  # 2021-02-08 21:52:06.902707
print(type(now))  # <class 'datetime.datetime'>

# 2. 获取指定日期和时间
dt = datetime(2021, 2, 8, 21, 55, 22)  # 用指定日期时间创建datetime
print(dt)  # 2021-02-08 21:55:22

# 3. datetime 转换 timestamp
# 北京时间 timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
# 计算机存储当前时间是以timestamp表示的

dt2 = datetime(2021, 2, 8, 22, 5, 20)
print(dt2.timestamp())  # 1612793120.0
# 注意Python的timestamp是一个浮点数，如果有小数位，小数位表示毫秒数

# 4. timestamp 转换为 datetime
t = dt2.timestamp()
print(datetime.fromtimestamp(t))  # 2021-02-08 22:05:20 本地时间
print(datetime.utcfromtimestamp(t))  # 2021-02-08 14:05:20 utc时间

# 5. str 转换为 datetime
cday = datetime.strptime('2021-2-8 22:15:55', '%Y-%m-%d %H:%M:%S')
print(cday)  # 2021-02-08 22:15:55
print(type(cday))  # <class 'datetime.datetime'>

# 6. datetime 转 str
print(now.strftime('%a, %b %d %H:%M'))  # Mon, Feb 08 22:09

# 7. datetime 加减
from datetime import timedelta

print(now)  # 2021-02-08 22:12:41.425628

print(now + timedelta(hours=10))  # 2021-02-09 08:12:41.425628
print(now - timedelta(days=1))  # 2021-02-07 22:12:41.425628
print(now + timedelta(days=2, hours=12))  # 2021-02-11 10:12:41.425628

# 8. 本地时间转换UTC时间
from datetime import timezone

tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
print(datetime.now())
dt = now.replace(tzinfo=tz_utc_8)
print(dt)  # 2021-02-08 23:19:35.618157+08:00

# 9. 时区转换
# utcnow()拿到当前的UTC时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc_dt', utc_dt)
# astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('bj_dt', bj_dt)
# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt', tokyo_dt)
# astimezone()将bj_dt转换为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt2', tokyo_dt2)

# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换
