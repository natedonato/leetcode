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
var insertGreatestCommonDivisors = function(head) {
    let node = head;
    while(node && node.next){
        const currentVal = node.val;
        const nextVal = node.next.val;
        const gcd = euclidianGCD(currentVal, nextVal);
        
        const newNode = new ListNode(gcd, node.next);
        node.next = newNode;
        
        node = newNode.next;
    }
    
    return head;
};

function euclidianGCD(a, b){
    while (b !== 0){
        const t = b
        b = a % b
        a = t
    }
    return a
}
