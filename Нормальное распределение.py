import random
import math


def main():
    print("=" * 40)
    print("   НОРМАЛЬНОЕ РАСПРЕДЕЛЕНИЕ")
    print("=" * 40)

    mu = float(input("Среднее значение: "))
    sigma = float(input("Стандартное отклонение: "))
    n = int(input("Сколько чисел сгенерировать: "))

    numbers = []

    for _ in range(n):
        u1 = random.random()
        u2 = random.random()
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        x = mu + sigma * z
        numbers.append(x)

    # Простая статистика
    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 40)

    print(f"\nСреднее: {sum(numbers) / n:.2f}")
    print(f"Мин: {min(numbers):.2f}")
    print(f"Макс: {max(numbers):.2f}")

    # Показываю все числа
    if n <= 20:
        print(f"\nСгенерированные числа:")
        for i, num in enumerate(numbers, 1):
            print(f"  {i}. {num:.2f}")
    else:
        print(f"\nПервые 10 чисел:")
        for i in range(10):
            print(f"  {i + 1}. {numbers[i]:.2f}")
        print(f"  ... и еще {n - 10} чисел")

    in_1sigma = sum(1 for x in numbers if abs(x - mu) < sigma)
    in_2sigma = sum(1 for x in numbers if abs(x - mu) < 2 * sigma)

    print(f"\nПопадание в интервал μ±σ: {in_1sigma}/{n} ({in_1sigma / n * 100:.1f}%)")
    print(f"Попадание в интервал μ±2σ: {in_2sigma}/{n} ({in_2sigma / n * 100:.1f}%)")


main()
