import math
import time

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  
    return math.sqrt(number)

number = 25100
delay = 2123  

result = delayed_sqrt(number, delay)

print(f"Квадратный корень из {number} после {delay} миллисекунд: {result}")
