class Node:
    # Create a node that stores data
    def __init__(self, data):
        self.data = data
        self.next = None

# In this head is None
class List:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode

    # Print values
    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    # Delete n nodes after m
    def deletenafterm(self, m, n):
        current = self.head
        while current:
            # Skip m nodes
            for _ in range(m - 1):
                if current is None:
                    return
                current = current.next

            if current is None or current.next is None:
                return
            temp = current.next
            for _ in range(n):
                if temp is None:
                    break
                temp = temp.next
                
            current.next = temp
            current = temp


# Example
llist = List()
nodes = [7, 8, 4, 3, 6, 5, 2]  # Example numbers
for node in nodes:
    llist.add(node)

print("Original Linked List:")
llist.show()

m, n = 2, 1  # Example numbers
llist.deletenafterm(m, n)

print("Modified Linked List after deleting", n, "nodes after skipping", m, "nodes:")
llist.show()
