import math
import tkinter as tk
from turtle import TurtleScreen, RawTurtle


def f(x):
    """Функция f(x) = x^2 + 4*sin(x) + 1"""
    return x ** 2 + 4 * math.sin(x) + 1


# ===== ЧАСТЬ 1: ОТДЕЛЕНИЕ КОРНЕЙ =====
x_start = -10
x_end = 10
step = 0.5

print("Практическая работа №2")
print("Отделение корней нелинейного уравнения f(x) = x^2 + 4*sin(x) + 1 = 0")
print("=" * 75)
print(f"{'x':<10} {'f(x)':<15} {'f(x+h)':<15} {'f(x)*f(x+h)':<15} {'Результат':<15}")
print("=" * 75)

roots_intervals = []
x = x_start

while x < x_end:
    f_x = f(x)
    f_x_next = f(x + step)
    product = f_x * f_x_next

    result = ""
    if product < 0:
        result = "КОРЕНЬ!"
        roots_intervals.append((x, x + step))

    print(f"{x:<10.2f} {f_x:<15.6f} {f_x_next:<15.6f} {product:<15.6f} {result:<15}")
    x += step

print("=" * 75)
print(f"\nНАЙДЕНО ИНТЕРВАЛОВ С КОРНЯМИ: {len(roots_intervals)}")
for i, (a, b) in enumerate(roots_intervals, 1):
    print(f"  {i}. Интервал [{a:.2f}, {b:.2f}]")

# ===== ЧАСТЬ 2: ПОСТРОЕНИЕ ГРАФИКА (ИСПРАВЛЕНО) =====
root = tk.Tk()
root.title("График функции f(x) = x² + 4sin(x) + 1")

# Создаем холст (Canvas) заданного размера
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Создаем экран Turtle внутри холста
screen = TurtleScreen(canvas)
# Убрана строка screen.setup(), так как размер берется из canvas
screen.setworldcoordinates(-12, -5, 12, 110)

# Создаем черепашку
pen = RawTurtle(screen)
pen.speed(0)
pen.hideturtle()

# Рисуем оси координат
pen.color("black")
pen.width(2)
# Ось X
pen.up()
pen.goto(-11, 0)
pen.down()
pen.goto(11, 0)
# Ось Y
pen.up()
pen.goto(0, -2)
pen.down()
pen.goto(0, 105)

# Подписи осей
pen.up()
pen.goto(10.5, -3)
pen.write("x", font=("Arial", 12, "normal"))
pen.goto(-1, 100)
pen.write("f(x)", font=("Arial", 12, "normal"))

# Рисуем график функции
pen.color("blue")
pen.width(2)
pen.up()

x_plot = -10
first_point = True

while x_plot <= 10:
    y_plot = f(x_plot)

    if first_point:
        pen.goto(x_plot, y_plot)
        pen.down()
        first_point = False
    else:
        pen.goto(x_plot, y_plot)

    x_plot += 0.1

# Отмечаем интервалы с корнями
pen.width(1)
for a, b in roots_intervals:
    pen.up()
    # Рисуем красный отрезок на оси X
    pen.goto(a, 0)
    pen.color("red")
    pen.down()
    pen.width(4)
    pen.goto(b, 0)
    pen.width(1)

    # Подпись интервала
    pen.up()
    pen.goto((a + b) / 2, -4)
    pen.write(f"[{a:.1f}, {b:.1f}]", align="center", font=("Arial", 9, "normal"))

# Заголовок
pen.up()
pen.goto(0, 100)
pen.color("black")
pen.write("f(x) = x² + 4sin(x) + 1", align="center", font=("Arial", 14, "bold"))

print("\n" + "=" * 75)
print("Готово. График построен в отдельном окне.")
print("=" * 75)

root.mainloop()
