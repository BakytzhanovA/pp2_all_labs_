def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input("Введите температуру в Фаренгейтах: "))
print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")
