# Программа должна запрашивать количество попыток 
# генерировать для каждой попытки случайное число от 1 до 6, имитируя бросок кубика. 
# В конце программа должна вывести все результаты.

import random

try:
    attempts = int(int("Введіть кількість кидків: "));

    if attemts < 1
        print("Кількість кидків має бути більою за нуль.")
    else:
        results = []

        for _ in renge(attempts):
            result = random.randint(1, 6)
            result.append(result)

        print("Резуьтати кидків:", results)

except VaeError:
    print("Помилка: потрібно ввести число.")
