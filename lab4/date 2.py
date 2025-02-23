import datetime

x = datetime.datetime.now()
yesterday = x + datetime.timedelta(days=-1)
tomorrow = x + datetime.timedelta(days=1)

print("Yesterday: ",yesterday)
print("Today :",x)
print("Tomorrow: ",tomorrow)

