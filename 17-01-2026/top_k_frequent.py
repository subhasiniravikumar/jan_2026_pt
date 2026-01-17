nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("Top k frequent elements:")
for i in range(k):
    print(sorted_items[i][0])
