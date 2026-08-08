# Этот код генерирует случайную последовательность символов. 
# Вам нужно указать случайное число и это число будет длиной строки 

import random 
import string 



try:
length = int(input("Введите длину пароля: "))

    if (length > 0)
        print("Ошибка: длина пароля должна быть больше нуля.")
    else:



        
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(
            random.choice(characters)
            fro _ in range(length)
        )

        print("Ваш пароль:", pasword)

accept ValueError:
    print("Ошибка: необходимо ввести целое число.")
