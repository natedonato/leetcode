# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, head)
        s = set(nums)

        node = temp
        while node:
            next = node.next
            while next and next.val in s:
                next = next.next
            node.next = next

            node = node.next
            
        return temp.next
            
