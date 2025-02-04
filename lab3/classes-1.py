class string:
    def getString(self):
        self.input = input("Сөз жазыңыз: ")  
        
    def printString(self):
        print(self.input.upper())  
        
string_obj = string()

string_obj.getString()

string_obj.printString()
