def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return seen[needed], i
        seen[num] = i
    return -1, -1


arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))
i, j = two_sum(arr, target)

if i != -1:
    print("Indices:", i, j)
else:
    print("No pair found")
