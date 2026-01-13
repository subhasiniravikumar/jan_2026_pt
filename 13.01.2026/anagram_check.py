s1 = input("First string: ").replace(" ", "").lower()
s2 = input("Second string: ").replace(" ", "").lower()

if len(s1) != len(s2):
    print("Not Anagrams")
else:
    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            print("Not Anagrams")
            break
        freq[ch] -= 1
    else:
        print("Anagrams")
