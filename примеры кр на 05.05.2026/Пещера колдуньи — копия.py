import sys

lines = [line.rstrip('\n') for line in sys.stdin]

def process(s):
    # удаляем каждый 4-й символ (индексы 3, 7, 11, ...)
    return ''.join(ch for i, ch in enumerate(s) if (i + 1) % 4 != 0)

processed = {process(line) for line in lines if line}  # убираем пустые строки
for line in sorted(processed):
    print(line)
