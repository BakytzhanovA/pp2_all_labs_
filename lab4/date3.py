import datetime
x = datetime.datetime.now()

x_without_microseconds = x.replace(microsecond=0)

print("Datetime without microseconds:", x_without_microseconds)
