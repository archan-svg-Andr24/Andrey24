from collections import Counter

nums = list(map(int, input().split()))
nums.sort()
n = len(nums)
median = nums[n // 2]

counter = Counter(nums)
mode = max(counter, key=lambda x: (counter[x], -nums.index(x)))
print(median, mode)