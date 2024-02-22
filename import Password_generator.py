import Password_generator

password = Password_generator.Password(16)
password1 = password.generate_password()

password2 = Password_generator.Password(16).generate_password()

print(password1)
print(password2)