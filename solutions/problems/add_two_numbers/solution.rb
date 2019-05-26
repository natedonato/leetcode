# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    node1 = l1
    node2 = l2
    l3 = ListNode.new(0);
    node3 = l3
    overflow = 0
    
     while (node1 && node2)
         val = node1.val + node2.val + node3.val
        node3.val = val % 10
        overflow = val / 10
         node1 = node1.next
         node2 = node2.next
         if(node1 || node2 || overflow != 0)
            node3.next = ListNode.new(overflow);
            node3 = node3.next
         end
    end
    
    node = node1 if node1
    node = node2 if node2
    
    while node
        val = node.val + node3.val
        node3.val = val % 10
        overflow = val / 10
        node = node.next
        if(node || overflow != 0)
            node3.next = ListNode.new(overflow);
            node3 = node3.next
        end
 
    end
        
        
    return l3
    
end