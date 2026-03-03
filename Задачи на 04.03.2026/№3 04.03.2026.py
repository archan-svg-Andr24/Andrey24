n = int(input())
lines = [input().strip() for _ in range(n)]
check_number = input().strip()


def is_valid_troll(num, check):
    num_str = str(num)
    for digit in check:
        if digit in num_str:
            return False
    return True


for line in lines:
    numbers = list(map(int, line.split(' & ')))
    odd_numbers = [num for num in numbers if num % 2 != 0 and is_valid_troll(num, check_number)]
    if odd_numbers:
        print(max(odd_numbers))
    else:
        print()
