'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        tail=head
        length=1
        while tail.next is not None:
            length+=1 
            tail=tail.next 
        k=k%length 
        if k==0:
            return head
        cur=head 
        count=0
        while cur is not None and count!=length-(k+1):
            count+=1 
            cur=cur.next 
        tail.next=head 
        head=cur.next
        cur.next=None
        return head

