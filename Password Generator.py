import string
import random

class password:
    def __init__(self, length, is_lower=True, is_upper=False, is_number=False, is_special=False):
        self.length     = length
        self.is_lower   = is_lower
        self.is_upper   = is_upper
        self.is_number  = is_number
        self.is_special = is_special

    def generatePassword(self):
        password = ''
        usableSymbols = ''

        if self.is_lower == True:
            usableSymbols += string.ascii_lowercase
        if self.is_upper == True:
            usableSymbols += string.ascii_uppercase
        if self.is_number == True:
            usableSymbols += string.digits
        if self.is_special == True:
            usableSymbols += string.punctuation

        for i in range(self.length):
            password += random.choice(usableSymbols)
        return password
    
password1 = password(16, is_number = True)
print(password1.generatePassword())