from enum import Enum
import random
import string


class Symbols_Qty(Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Eleven = 11
    # есть ли шаблон чтобы динамически генерить Enum?

class Creds_Generator:
    @staticmethod
    def generate_random_name():
        MIN_Qty_Symbols = Symbols_Qty.One
        MAX_Qty_Symbols = Symbols_Qty.Eleven
        length = random.randint(MIN_Qty_Symbols, MAX_Qty_Symbols)
        characters = string.ascii_letters
        name = ''.join(random.choices(characters, k=length))
        return name

    @staticmethod
    def generate_random_password(name):
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        cyrillic_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        digits = string.digits
        password = random.choices(lowercase_letters + uppercase_letters + cyrillic_letters, k=10)
        password[random.randint(0, 8)] = random.choice(lowercase_letters)
        password[random.randint(0, 8)] = random.choice(uppercase_letters)
        password[random.randint(0, 8)] = random.choice(cyrillic_letters)
        password[random.randint(0, 8)] = random.choice(digits)
        password.append(random.choice(name))
        password = ''.join(password)
        return password

