/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let firstPointer = head;
    let secondPointer = head;
    for(let i = 0; i < n; i++){
        firstPointer = firstPointer.next;
    }
    
    if(!firstPointer){
        return secondPointer.next
    }
    while(firstPointer.next){
        firstPointer = firstPointer.next
        secondPointer = secondPointer.next
    }
    
    secondPointer.next = secondPointer.next.next
    
    return head;
};