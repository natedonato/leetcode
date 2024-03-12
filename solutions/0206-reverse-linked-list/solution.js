/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if(head === null){
        return null;
    }
    let prev = null;
    let current = head;
    let next = current.next;
        
    while(next !== null){
        current.next = prev;
        prev = current;
        current = next;
        next = current.next;
    }
    
    current.next = prev;
    return current;
};
