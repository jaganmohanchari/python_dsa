"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
"""

def startNodeCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

"""
def array_to_LL(arr, n):
    if n == 0:
        return None
    head = Node(arr[0])
    cur = head
    for i in range(1, n):
        temp = Node(arr[i])
        cur.next = temp
        cur = cur.next
    return head

def convert_to_cycle(head, k):
    temp = head
    count = 0
    cycle_node = None
    while temp:
        if count == k:
            cycle_node = temp
        count += 1
        temp = temp.next
    if cycle_node is None:
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = cycle_node
    return head

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    head = array_to_LL(arr, n)
    head = convert_to_cycle(head, k)
    result = startNodeCycle(head)
    if result:
        print(result.data)
    else:
        print("NULL")
"""