# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head 

        l = 1
        n = head
        while n.next:
            l += 1
            n = n.next

        k %= l
        if k == 0:
            return head 

        n.next = head
        m = head
        for i in range(l - k - 1):
            m = m.next
        
        head = m.next
        m.next = None
        return head
        
    
