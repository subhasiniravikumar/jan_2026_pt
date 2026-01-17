s = input("Enter expression: ")

stack = []
pairs = {')': '(', '}': '{', ']': '['}
balanced = True

for ch in s:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if not stack or stack.pop() != pairs[ch]:
            balanced = False
            break

if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")
