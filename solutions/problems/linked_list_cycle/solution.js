/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let slow = head;
    let fast = head;

    while(fast !== null && fast.next !== null){
        fast = fast.next;
        if(fast === slow){
            return true
        }
        fast = fast.next;
        if(fast === slow){
            return true
        }
        slow = slow.next;
    }
    return false;
};