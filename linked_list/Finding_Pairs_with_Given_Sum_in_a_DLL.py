'''
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
'''

def getPairs(head, val):
    ans = []
    left = head
    right = head
    while right.next:
        right = right.next
    while left.data < right.data:
        x = left.data + right.data
        if x == val:
            ans.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif x < val:
            left = left.next
        else:
            right = right.prev
    return ans

'''
def arrayToDLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        temp.prev = cur
        cur.next = temp
        cur = temp
    return head



if __name__ == "__main__":
    arr = [2, 3, 4, 5, 7, 8, 10, 13]
    head = arrayToDLL(arr)
    ans = getPairs(head, 10)
    for x in ans:
        print(x[0], x[1])
'''