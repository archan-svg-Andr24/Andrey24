import numpy as np

def f(x):
    """Исходная функция f(x) = x² + 4sin(x) + 1"""
    return x**2 + 4*np.sin(x) + 1

def df(x):
    """Производная f'(x) = 2x + 4cos(x)"""
    return 2*x + 4*np.cos(x)

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    Метод Ньютона (метод касательных) для решения f(x) = 0

    Параметры:
    f - функция
    df - производная функции
    x0 - начальное приближение
    tol - требуемая точность
    max_iter - максимальное число итераций

    Возвращает:
    x - найденный корень
    iterations - список итераций
    """
    x = x0
    iterations = []

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        iterations.append((i, x, fx))

        if abs(fx) < tol:
            print(f"Сходимость за {i+1} итераций")
            break

        if abs(dfx) < 1e-10:
            print("Производная близка к нулю!")
            break

        x = x - fx / dfx

    return x, iterations

# Решение
print("Уравнение: x² + 4sin(x) + 1 = 0\n")

# Первый корень
print("Корень 1 (x₀ = -2):")
root1, _ = newton_method(f, df, -2.0)
print(f"x₁ = {root1:.10f}")
print(f"Проверка: f(x₁) = {f(root1):.3e}\n")

# Второй корень
print("Корень 2 (x₀ = -0.3):")
root2, _ = newton_method(f, df, -0.3)
print(f"x₂ = {root2:.10f}")
print(f"Проверка: f(x₂) = {f(root2):.3e}")