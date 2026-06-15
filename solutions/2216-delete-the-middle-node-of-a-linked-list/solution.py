# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        l = 0
        node = head 
        while node:
            node = node.next
            l += 1

        mid = l // 2

        node = head
        for i in range(mid - 1):
            node = node.next

        node.next = node.next.next
        return head
        
