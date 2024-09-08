/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode[]}
 */
var splitListToParts = function(head, k) {
    let length = 0;
    let p = head;
    while(p){
        length += 1;
        p = p.next;
    }
    
    const fraction = Math.floor(length / k);
    let remainder = length % k;
    
    // console.log(fraction, remainder);
    
    const output = [];
    
    let node = head;
    
    for(let i = 0; i < k; i++){
        let size = fraction
        if(remainder > 0){
            size += 1;
            remainder -= 1;
        }
        let [p1,p2] = makeSegment(size, node);
        output.push(p1);
        node = p2;
    }
    
    function makeSegment(size, node){
        if(!node){
            return [null, null];
        }
        let head = node;
        
        for(let i = 1; i < size; i++){
            
            if(node){
                node = node.next
            }
        }
        
        if(node){
            let temp = node.next;
            node.next = null;
            node = temp;
        }
        
        return [head , node];
    }
    
    return output;
};
