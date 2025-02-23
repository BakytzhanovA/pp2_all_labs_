import datetime

x = datetime.datetime.now()
after_subtract_5days = x + datetime.timedelta(days=-5)

print("Current date: ",x)
print("After subtract 5 days: ",after_subtract_5days)