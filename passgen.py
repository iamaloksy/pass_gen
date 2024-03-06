import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

pass_list = letters + digits + special_chars
password_len = int(input("enter length"))

password = ''
for i in range(password_len):
    password += ''.join(secrets.choice(pass_list))

print(password)
