/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    let pqueue = [p];
    let qqueue = [q];
    
    
    while(pqueue.length > 0 && qqueue.length > 0){
        let nodep = pqueue.shift();
        let nodeq = qqueue.shift();
        
        if(nodep === null || nodeq === null || nodep === undefined || nodeq === undefined){
            if(nodep !== nodeq){
                return false;
            }   
        }else if(nodep.val !== nodeq.val){
            return false;
        }else{
            pqueue.push(nodep.left);
            pqueue.push(nodep.right)
            qqueue.push(nodeq.left);
            qqueue.push(nodeq.right);
        }
        
    }
    
    
    return (pqueue.length === 0 && qqueue.length === 0);
};