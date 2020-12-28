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
var goodNodes = function(root) {
    let max = [];
    let count = 0;
    
    dfs(root);
    
    function dfs(node){
        if(max.length < 1){
            max.push(node.val)
            node.left && dfs(node.left);
            node.right && dfs(node.right);
            count += 1;
        }else{
            let last = max[max.length - 1]
            if(last <= node.val){
                count += 1;
            }
            max.push(Math.max(node.val, last));
            node.left && dfs(node.left);
            node.right && dfs(node.right);
            max.pop(); 
        }
    }
    return count;
};