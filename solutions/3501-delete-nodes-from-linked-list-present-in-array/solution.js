/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function(nums, head) {
    const s = new Set(nums)


    let node = head;
    while(node.next){
        if(s.has(node.next.val)){
            node.next = node.next.next

        }else{
            node = node.next
        }
    }
    if(s.has(head.val)){
        head = head.next
    }
    return head
};
