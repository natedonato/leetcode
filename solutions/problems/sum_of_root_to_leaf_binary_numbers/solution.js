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
 * @return {number}
 */
var sumRootToLeaf = function(root) {
    let path = [];
    let sum = 0;
    
    dfs(root);
    
    
    function dfs(node){
        path.push(node.val);
        
        if(!node.left && !node.right){
            bstring = path.join('')
            sum += parseInt(bstring, 2);
        }else{
            node.left && dfs(node.left);
            node.right && dfs(node.right);
        }
        path.pop(node.val);
    }
    return sum;
};