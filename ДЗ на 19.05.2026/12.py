lines = []
while True:
    s = input()
    if s == '':
        break

    result_chars = []
    for i in range(len(s)):
        if (i + 1) % 5 != 0:
            result_chars.append(s[i])
    s = ''.join(result_chars)

    if s not in lines:
        lines.append(s)

# Сортировка: сначала короткие, при равной длине — по алфавиту
print('\n'.join(sorted(lines, key=lambda x: (len(x), x))))