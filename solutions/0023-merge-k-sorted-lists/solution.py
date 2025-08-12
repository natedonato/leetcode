# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(-1)
        node = head

        h = []
        count = 0
        for list in lists:
            if list is not None:
                heapq.heappush(h, (list.val, count, list))
                count += 1

        while h:
            next_node = heapq.heappop(h)[2]
            if next_node is None:
                break
            
            node.next = next_node
            node = next_node
            if next_node.next is not None:
                heapq.heappush(h, (next_node.next.val, count, next_node.next))
                count += 1
        
        return head.next
