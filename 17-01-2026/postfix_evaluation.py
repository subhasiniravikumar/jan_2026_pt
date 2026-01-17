expr = input("Enter postfix expression: ").split()
stack = []

for token in expr:
    if token.isdigit():
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()
        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
        elif token == '/':
            stack.append(a // b)

print("Result:", stack[0])
