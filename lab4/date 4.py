import datetime

first_date = datetime.datetime(2020,9,5,15,3,10)
second_date = datetime.datetime.now()

difference = abs(first_date - second_date).total_seconds()

print("Difference",difference,"seconds")