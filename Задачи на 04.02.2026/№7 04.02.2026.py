
def print_average(arr):
    if not arr:
        print(0)
    else:
        print(sum(arr) / len(arr))


def _median(arr):
    s = sorted(arr)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return float(s[mid])
    return (s[mid - 1] + s[mid]) / 2


def print_statistics(arr):
    if not arr:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        return

    print(len(arr))
    print(sum(arr) / len(arr))  
    print(min(arr))
    print(max(arr))
    print(_median(arr))


print_statistics([])