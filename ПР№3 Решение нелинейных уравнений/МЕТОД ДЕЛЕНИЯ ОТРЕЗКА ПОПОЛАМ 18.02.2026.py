import numpy as np

def f(x):
    return x**2 + 4*np.sin(x) + 1

def bisection_method(a, b, tol=0.001):
    iteration = 0
    print(f"\nРешение для интервала [{a}, {b}] с точностью {tol}")
    print(f"| № | {'a':^9} | {'b':^9} | {'x (сер.)':^9} | {'f(x)':^9} | {'Действие':^9} |")
    print("|---|-----------|-----------|------------|-----------|-----------|")

    while (b - a) / 2 > tol:
        iteration += 1
        c = (a + b) / 2
        fc = f(c)
        fa = f(a)

        if fa * fc < 0:
            action = "b = x"
            next_b = c
            next_a = a
        else:
            action = "a = x"
            next_a = c
            next_b = b

        print(f"| {iteration} | {a:9.4f} | {b:9.4f} | {c:9.4f} | {fc:9.4f} | {action:9} |")

        a, b = next_a, next_b

    final_x = (a + b) / 2
    print(f"\nИтог: x ≈ {final_x:.4f}")
    return final_x

# Запуск
bisection_method(-2.0, -1.5)
bisection_method(-0.5, 0.0)