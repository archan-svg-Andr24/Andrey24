s = input()
count = sum(1 for c in s if c not in (' ', '\t'))
print(count)