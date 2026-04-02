import numpy as np

# Исходные точки
x_known = np.array([10, 20, 30, 40, 50])  # точки икс
y_known = np.array([100, 200, 300, 400, 500])  # точки игрек

# Точка-посерединка
x_new = 25

# Линейная интерполяция
y_new = np.interp(x_new, x_known, y_known)
print(y_new)  # 250.0
