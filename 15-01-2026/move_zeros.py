arr = list(map(int, input("Enter array: ").split()))

pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print("Result:", arr)
