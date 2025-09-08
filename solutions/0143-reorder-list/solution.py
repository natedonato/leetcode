# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next
        
        n = len(arr)

        front_node = head
        for i in range(0, n//2):
            back_node = arr.pop()
            arr[-1].next = None
            back_node.next = front_node.next
            front_node.next = back_node
            front_node = back_node.next
