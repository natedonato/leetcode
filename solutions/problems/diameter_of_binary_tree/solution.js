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
var diameterOfBinaryTree = function(root) {
    if(!root){return 0;}
    if(!(root.left || root.right)){return 0;}
    
    const left = root.left
    const right = root.right

    var depthFinder = function(node) {
        if(!node){return 0;}
        return 1 + Math.max(depthFinder(node.left), depthFinder(node.right))
    }
    
           
    let depth_left = depthFinder(left)
    let depth_right = depthFinder(right)
    let root_to_leaves_path = depth_left + depth_right
    
    
    return Math.max(diameterOfBinaryTree(left), diameterOfBinaryTree(right), root_to_leaves_path)
};