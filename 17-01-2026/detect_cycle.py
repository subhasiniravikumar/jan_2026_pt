class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Sample test
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = b   # creates cycle

print("Cycle present:", has_cycle(a))
