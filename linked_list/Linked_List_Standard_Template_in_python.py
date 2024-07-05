class Node:
    def __init__(self, value=0, next_node=None):
        self.data = value
        self.next = next_node

p1 = Node(5, None)
p2 = Node(7)
p3 = Node()

print(p1.data)  # 5
print(p2.data)  # 7
print(p3.data)  # 0