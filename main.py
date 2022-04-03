from random import choice
import clipboard
digits = '0123456789'
chars = 'abcdefgh1jkmn0pqrstuvwxyz'
up = chars.upper()
specials = '!@$%&'
All = digits + chars + up + specials

password = ''.join(choice(All) for i in range(10))
clipboard.copy(password)
print(password)
