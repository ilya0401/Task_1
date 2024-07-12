from enum import Enum
import random
import string


class Generate_Creds:
    def generate_random_name():
        # определить набор символов для имени, который включает строчные буквы, прописные буквы
        characters = string.ascii_letters

        # генерю рандомную длину от 5 до 10 символов
        length = random.randint(5, 10)

        # создаю случайное имя, выбрав символы из определенного набора символов.
        name = ''.join(random.choices(characters, k=length))

        return name

    # создаю переменную
    random_name = generate_random_name()
    # print(random_name)

    # строку в список, чтобы потом из списка брать букву
    random_name_list = list(random_name)
    # print(random_name_list)

    def generate_random_password(self):
        # определить набор символов для имени, который включает строчные буквы, прописные буквы
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits

        # генерю пароль с миним 10 символами
        password = random.choices(lowercase_letters + uppercase_letters + digits, k=10)

        # убедиться что условия выполнены
        password[random.randint(0, 8)] = random.choice(lowercase_letters)
        password[random.randint(0, 8)] = random.choice(uppercase_letters)
        password[random.randint(0, 8)] = random.choice(digits)
        # добавляю букву из имени почты, чтобы удовлетворить условие
        password.append(self.random_name_list[0])

        # перевожу список в строку
        password = ''.join(password)


        return password

    random_password = generate_random_password()
    # print(random_password)

