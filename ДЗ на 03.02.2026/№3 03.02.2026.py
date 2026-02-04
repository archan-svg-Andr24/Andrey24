n = int(input())

for _ in range(n):
    cubes = list(map(int, input().split()))

    result = []
    left = 0
    right = len(cubes) - 1
    last = float('inf')

    possible = True

    while left <= right:
        left_ok = (cubes[left] <= last)
        right_ok = (cubes[right] <= last)

        if left_ok and right_ok:
            if cubes[left] >= cubes[right]:
                result.append(cubes[left])
                last = cubes[left]
                left += 1
            else:
                result.append(cubes[right])
                last = cubes[right]
                right -= 1
        elif left_ok:
            result.append(cubes[left])
            last = cubes[left]
            left += 1
        elif right_ok:
            result.append(cubes[right])
            last = cubes[right]
            right -= 1
        else:
            possible = False
            break

    if not possible:
        print("НЕТ")
    else:
        print(" ".join(map(str, result)))