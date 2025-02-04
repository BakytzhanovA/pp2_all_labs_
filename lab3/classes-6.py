class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers  
        
    #jai san proverka
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

obj_prime_filter = PrimeFilter(numbers)

# jai sandar tizimi
prime_numbers = obj_prime_filter.filter_primes()

# res
print("Простые числа:", prime_numbers)
