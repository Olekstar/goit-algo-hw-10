import numpy as np
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Визначення меж інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа
max_f = 4  # Максимальне значення функції на вказаному інтервалі

# Генерація випадкових точок
n = 100000  # Кількість випадкових точок
random_x = np.random.uniform(a, b, n)
random_y = np.random.uniform(0, max_f, n)

# Підрахунок кількості точок, які попадають під криву
count_under_curve = np.sum(random_y <= f(random_x))

# Обчислення співвідношення кількості точок під кривою до загальної кількості точок
ratio = count_under_curve / n

# Обчислення оцінки площі під кривою
area = ratio * (b - a) * max_f

print("Оцінка інтеграла методом Монте-Карло:", area)

# Аналітичне обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Аналітичний розв'язок інтеграла: ", result)