/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSubPath = function(head, root) {
    const queue = [root];
    
    while(queue.length > 0){
        const n = queue.shift();
        if(testNode(n) === true){
            return true;
        }
        n.left && queue.push(n.left);
        n.right && queue.push(n.right);
    }
    
    return false;
    
    function testNode(treeNode){
        let listNode = head;
        
        let queue = [treeNode];
        
        while(queue.length > 0){
            const l = queue.length;l
            for(let i = 0; i < l; i++){
                treeNode = queue.shift();
                
                if(treeNode.val !== listNode.val){
                    continue;
                }
                
                if(!listNode.next){
                    return true;
                }
                
                if(treeNode.left){
                    queue.push(treeNode.left)
                }
                if(treeNode.right){
                    queue.push(treeNode.right);
                }
            }
            listNode = listNode.next;
        }
        return false;
    }
};
