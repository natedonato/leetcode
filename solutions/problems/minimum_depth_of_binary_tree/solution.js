/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    if(!root){
       return 0;
    };
    if(!root.left && !root.right){
        return 1;
    }
    let depth = 1;
    let bestDepth = Infinity;
    if(root.left){
        dfsUtil(root.left, depth);
    }
    if(root.right){
        dfsUtil(root.right, depth);
    }
    
    function dfsUtil(node, depth){
        depth += 1;
        if(bestDepth <= depth){
            return;
        }
        if(!node.left && !node.right){
            if(depth < bestDepth){
                bestDepth = depth;
                return;
            }
        };
        
        if(node.left){
            dfsUtil(node.left, depth);
        };
        if(node.right){
            dfsUtil(node.right, depth)
        };  
    };
    
    return bestDepth;
};