nums = list(map(int, input("Enter numbers: ").split()))

n = len(nums)
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

print("Missing number:", expected_sum - actual_sum)
