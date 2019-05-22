/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
      return height(root) !== -1; 

    function height(node) {
        if (node === null) {
            return 0; 
        }

        let left = height(node.left); 
        let right = height(node.right); 
    
        if ( left === -1 || right === -1 || Math.abs(left - right) > 1) {
            return -1;
        }

        return 1 + Math.max(left, right); 
    }
};