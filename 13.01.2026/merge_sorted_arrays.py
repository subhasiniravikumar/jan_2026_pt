a = list(map(int, input("Array 1: ").split()))
b = list(map(int, input("Array 2: ").split()))

i = j = 0
merged = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])

print("Merged array:", merged)
