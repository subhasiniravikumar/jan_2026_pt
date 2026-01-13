arr = list(map(int, input("Enter numbers: ").split()))

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

if second == float('-inf'):
    print("Second largest not found")
else:
    print("Second largest:", second)
