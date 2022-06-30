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
var middleNode = function(head) {
    let p1 = head;
    let p2 = head;
    let i = 0;
    
    while(p1.next !== null){
        p1 = p1.next
        if(i % 2 == 0){
            p2 = p2.next;
        }
        i++;
    }
    
    return p2;
};