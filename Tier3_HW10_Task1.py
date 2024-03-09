from pulp import *

# Створення моделі
model = LpProblem("Максимізація продукції", LpMaximize)

# Визначення змінних рішення
limonad = LpVariable("Лимонад", lowBound=0, cat='Continuous')
fruktoviy_sik = LpVariable("Фруктовий сік", lowBound=0, cat='Continuous')

# Додавання цільової функції
model += limonad + fruktoviy_sik, "Загальна кількість продукції"

# Додавання обмежень
model += 2*limonad + fruktoviy_sik <= 100, "Обмеження води"
model += limonad <= 50, "Обмеження цукру"
model += limonad <= 30, "Обмеження лимонного соку"
model += 2*fruktoviy_sik <= 40, "Обмеження фруктового пюре"

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Виробити лимонаду для максимізації виробництва:", limonad.varValue)
print("Виробити фруктового соку для максимізації виробництва:", fruktoviy_sik.varValue)
print("Партія для максимальної загальної кількості продукції:", value(model.objective))
