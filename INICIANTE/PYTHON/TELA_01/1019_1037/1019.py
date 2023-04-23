import datetime
seconds = int(input())
str(datetime.timedelta(seconds=666))
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print(f'{h:d}:{m:01d}:{s:01d}')