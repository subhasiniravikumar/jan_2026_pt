arr = list(map(int, input("Enter array: ").split()))

current_sum = max_sum = arr[0]

for num in arr[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print("Maximum subarray sum:", max_sum)
