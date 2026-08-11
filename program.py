# Цей код створює випадкову послідовність символів.
# Вам потрібно вказати випадкове число і це число буде довжиною рядка



import random 
import string 



try:
    length = int(input("Введіть довжину пароля: "))

    if (length <= 0):
        print("Помилка: довжина пароля повинна бути більшою за нуль.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        print("Ваш пароль:", password)

except ValueError:
    print("Помилка: потрібно ввести ціле число.")
