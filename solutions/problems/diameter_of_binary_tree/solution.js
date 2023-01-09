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
    let dMax = 0;

    function dfsDiameter(node){
        if(!node){
            return 0
        }

        let left = dfsDiameter(node.left);
        let right = dfsDiameter(node.right);

        let d = left + right
        dMax = Math.max(d, dMax);

        return Math.max(left,right) + 1
    }
    dfsDiameter(root)
    return dMax
};