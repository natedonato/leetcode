# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1, head)
        prevnode = dummy
        currentnode = head
        nextnode = head.next
        
        while currentnode and nextnode:
            prevnode.next = nextnode
            currentnode.next = nextnode.next
            nextnode.next = currentnode
            prevnode = currentnode
            currentnode = currentnode.next
            
            if currentnode:
                nextnode = currentnode.next
        
        return dummy.next
        
