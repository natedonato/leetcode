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
 * @return {boolean}
 */
var isBalanced = function(root) {
    // return height or -1 if unbalanced

    var dfsHeight = function(node ){
        
        if(node === null){
            return 0;
        }

        let left = dfsHeight(node.left);

        let right = dfsHeight(node.right);

        if(left === -1 || right === -1 || Math.abs(left - right) > 1){
            return -1
        }

        return 1 + Math.max(left, right)
    }


    return dfsHeight(root) !== -1
};