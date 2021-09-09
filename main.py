from random import choice

digits = '0123456789'
chars = 'abcd3fgh1jklmn0pqrstuvwxyz'
up = chars.upper()
specials = '!@$%&'
All = digits + chars + up + specials

password = ''.join(choice(All) for i in range(8))

print(password)
