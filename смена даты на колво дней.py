import datetime
y,m,d=(int(n) for n in input().split())
days=datetime.timedelta(int(input()))
date=datetime.date(y,m,d)
print( (date+days).strftime("%Y %-m %-d"))