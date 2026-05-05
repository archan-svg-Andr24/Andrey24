import numpy as np
import matplotlib.pyplot as plt

# Данные варианта 1
x = [-1, 0, 3, 4]
y = [-3, 5, 2, -6]

# Функция Лагранжа
def lagrange(x_val):
    result = 0
    n = len(x)
    for i in range(n):
        # Вычисляем i-й базисный полином
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result

# Вычисляем в точке x = 2
x_inter = 2
y_inter = lagrange(x_inter)
print(f"L({x_inter}) = {y_inter}")

# Строим график
x_vals = np.linspace(-1.5, 4.5, 100)
y_vals = [lagrange(t) for t in x_vals]

plt.plot(x_vals, y_vals, 'b-', label='Полином Лагранжа')
plt.plot(x, y, 'ro', label='Узловые точки')
plt.plot(x_inter, y_inter, 'g*', markersize=12, label=f'x={x_inter}, y={y_inter}')
plt.grid(True)
plt.legend()
plt.show()