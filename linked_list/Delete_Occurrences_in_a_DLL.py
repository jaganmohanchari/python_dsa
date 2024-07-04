"""
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
"""

def deleteAllOccurrences(head, val):
    cur = head
    
    while cur:
        
        if cur.data == val:
            
            if cur == head:
                head = cur.next
                
            prev = cur.prev
            next = cur.next
            
            if prev:
                prev.next = next
            if next:
                next.prev = prev
                
            del cur
            cur = next
            
        else:
            cur = cur.next
            
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
    arr = [6, 2, 6, 3, 4, 5, 6]
    head = array_to_DLL(arr)
    
    val = 6
    head = deleteAllOccurrences(head, val)

    print_list(head)
"""