stack = []

while True:
    print("1.Push  2.Pop  3.Display  4.Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        stack.append(input("Enter element: "))
    elif choice == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")
    elif choice == 3:
        print("Stack:", stack)
    else:
        break
