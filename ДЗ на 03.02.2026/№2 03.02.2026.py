s = input().lower()
print(max(s.count(c) for c in set(s)))