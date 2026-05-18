lines = []
while True:
    s = input()
    if s == '':
        break

    result_chars = []
    for i in range(len(s)):
        if (i + 1) % 6 != 0:
            result_chars.append(s[i])
    s = ''.join(result_chars)

    # заменяем все пробелы на подчёркивания
    s = s.replace(' ', '_')

    # убираем дубликаты строк
    if s not in lines:
        lines.append(s)

print('\n'.join(sorted(lines)))
