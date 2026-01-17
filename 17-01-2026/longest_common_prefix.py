words = input("Enter words: ").split()

prefix = words[0]

for word in words[1:]:
    i = 0
    while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
        i += 1
    prefix = prefix[:i]

print("Longest Common Prefix:", prefix)
