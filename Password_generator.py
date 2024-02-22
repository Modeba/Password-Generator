import string
import random

class Password:
    def __init__(self, length, is_lower=True, is_upper=False, is_number=False, is_special=False):
        self.length     = length
        self.is_lower   = is_lower
        self.is_upper   = is_upper
        self.is_number  = is_number
        self.is_special = is_special

    def generate_password(self):
        password = ''
        usable_symbols = ''

        if self.is_lower:
            usable_symbols += string.ascii_lowercase
        if self.is_upper:
            usable_symbols += string.ascii_uppercase
        if self.is_number:
            usable_symbols += string.digits
        if self.is_special:
            usable_symbols += string.punctuation

        for i in range(self.length):
            password += random.choice(usable_symbols)
        return password
    
#password1 = Password(16, is_number = True)
#print(password1.generate_password())