/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var largestValues = function(root) {
    let max = [];
    
    let depth = -1;
    const dfs = (node) => {
        depth += 1;
        if(max[depth] === undefined){
            max[depth] = node.val;
        }else{
            max[depth] = Math.max(max[depth], node.val);
        }
        node.left !== null && dfs(node.left);
        node.right !== null && dfs(node.right);
        
        depth -= 1;
    }
    root && dfs(root);
    return max;
};