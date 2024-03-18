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
var diameterOfBinaryTree = function(root) {
    return dfsHelper(root)[0];
};

function dfsHelper(node){
    if(!node.left && !node.right){
        return [0,0];
    }

    let left = [-1, -1];
    let right = [-1, -1];

    if(node.left){
        left = dfsHelper(node.left);
    }
    if(node.right){
        right = dfsHelper(node.right);
    }

    let maxDepth = Math.max(left[1] + 1, right[1] + 1);

    let maxDiam = Math.max(left[0], right[0], (left[1] + right[1] + 2));

    return [maxDiam, maxDepth];
}
