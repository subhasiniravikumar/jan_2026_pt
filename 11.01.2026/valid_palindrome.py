s = input("Enter string: ")

clean = ""
for ch in s:
    if ch.isalnum():
        clean += ch.lower()

left, right = 0, len(clean) - 1
is_palindrome = True

while left < right:
    if clean[left] != clean[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print("Valid Palindrome" if is_palindrome else "Not a Palindrome")
