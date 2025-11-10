# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current_node = list1

        idx = 0
        while idx < a - 1:
            current_node = current_node.next
            idx += 1
        a = current_node

        while idx < b + 1:
            current_node = current_node.next
            idx +=1
        b = current_node

        a.next = list2
        current_node = list2
        while current_node.next:
            current_node = current_node.next

        current_node.next = b

        return list1
