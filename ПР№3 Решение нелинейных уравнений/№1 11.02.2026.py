import math


def f(x):
    return x ** 2 + 4 * math.sin(x) + 1


def bisection_solve(a, b, tolerance=1e-6):
    if f(a) * f(b) >= 0:
        print("На концах интервала функция должна иметь разные знаки!")
        return None

    mid = a
    while abs(b - a) > tolerance:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return mid


# Находим оба корня, задавая соответствующие интервалы
root1 = bisection_solve(-0.5, 0.5)
root2 = bisection_solve(-2.5, -1.0)

print(f"Корень 1: {root1:.6f}")
print(f"Корень 2: {root2:.6f}")
