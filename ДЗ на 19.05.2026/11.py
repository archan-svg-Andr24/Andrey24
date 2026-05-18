lines = []
while True:
    s = input()
    if s == '':
        break
    # Удаляем каждый третий символ
    result_chars = []
    for i in range(len(s)):
        if (i + 1) % 3 != 0:
            result_chars.append(s[i])
    s = ''.join(result_chars)

    if s not in lines:
        lines.append(s)

# Обратный алфавитный порядок
print('\n'.join(sorted(lines, reverse=True)))
