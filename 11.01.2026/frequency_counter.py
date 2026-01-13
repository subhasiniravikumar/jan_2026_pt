text = input("Enter text: ")

freq = {}

for ch in text:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

for key in freq:
    print(key, ":", freq[key])
