# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        m = -math.inf
        for i in range(len(arr) // 2 + 1):
            m = max(m, arr[i] + arr[-i - 1] )
        return m
