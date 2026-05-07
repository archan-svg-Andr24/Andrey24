x_points = [-1, 0, 3, 4]
y_points = [-3, 5, 2, -6]


# Функция для вычисления полинома Лагранжа в точке x = 2
def lagrange(x):
    n = 4
    result = 0

    for i in range(n):
        li = 1
        for j in range(n):
            if j != i:
                li = li * (x - x_points[j]) / (x_points[i] - x_points[j])
        result = result + y_points[i] * li

    return result


print("\nИсходные данные:")
print("x:", x_points)
print("y:", y_points)

x = 2
y = lagrange(x)
print(f"x = {x}: y = {round(y, 4)}")
