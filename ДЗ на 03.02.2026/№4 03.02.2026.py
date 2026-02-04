nums = list(map(float, input().split()))
n = len(nums)
nums.sort()
mean = sum(nums) / n
median = nums[n // 2] if n % 2 == 1 else (nums[n // 2 - 1] + nums[n // 2]) / 2
print(f"{mean} {median:.1f}")