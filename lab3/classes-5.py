class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner  
        self.balance = balance  

    # счетты толтыру
    def deposit(self, tg):
        if tg > 0:
            self.balance += tg 
            print(f"Пополнение на {tg} тенге. Текущий баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть больше нуля.")

    # ақшаны шешу
    def withdraw(self, tg):
        if tg > self.balance:
            print("Недостаточно средств на счете для этой операции.")
        elif tg > 0:
            self.balance -= tg  
            print(f"Снято {tg} тенге. Текущий баланс: {self.balance}")
        else:
            print("Сумма снятия должна быть больше нуля.")

account = Account("Алиш", 100)

account.deposit(50) #50 тг счетты толтырамыз

account.withdraw(30) #30 тг шешіп көреміз

# 150 тг шешіп көреміз (счетта бар суммадан көп)
account.withdraw(150)

account.withdraw(-10)
