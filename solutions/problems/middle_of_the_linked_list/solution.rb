# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {ListNode}
def middle_node(head)
    length = 1
    length_finder = head
    while length_finder.next != nil
        length += 1
        length_finder = length_finder.next
    end
    midpoint = length / 2 + 1
    i = 1
    middle_node = head
    while i < midpoint
        middle_node = middle_node.next
        i += 1
    end
    middle_node
    
end