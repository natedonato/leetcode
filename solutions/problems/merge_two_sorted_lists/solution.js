/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    if(!(l1 || l2)){
        return null;
    }
    if(!(l1 && l2)){
        return l1 || l2
    }
    let node = new ListNode();
    if(l1.val < l2.val){
        node.val = l1.val;
        node.next = mergeTwoLists(l1.next, l2);
    }else{
        node.val = l2.val;
        node.next = mergeTwoLists(l1, l2.next);
    }
    return node
};