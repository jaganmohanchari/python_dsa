"""
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
"""

def removeDuplicates(head):
    cur = head.next

    while cur:
        prev = cur.prev
        next = cur.next

        if cur.data == prev.data:
            prev.next = next
            if next:
                next.prev = prev

            del cur

        cur = next

    return head

"""
def array_to_DLL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    cur = head

    for data in arr[1:]:
        temp = Node(data)
        temp.prev = cur
        cur.next = temp
        cur = temp

    return head

def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    arr = [5, 7, 7, 9, 10, 11]
    head = array_to_DLL(arr)
    head = removeDuplicates(head)
    print_list(head)
"""

#inputs

#6 input-size 
#array 5 7 7 9 10 11 
#6
#3 3 3 5 6 6