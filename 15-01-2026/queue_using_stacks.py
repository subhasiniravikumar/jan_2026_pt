stack1 = []
stack2 = []

def enqueue(x):
    stack1.append(x)

def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    return stack2.pop() if stack2 else "Queue Empty"

while True:
    print("1.Enqueue 2.Dequeue 3.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        enqueue(input("Enter value: "))
    elif ch == 2:
        print("Removed:", dequeue())
    else:
        break
