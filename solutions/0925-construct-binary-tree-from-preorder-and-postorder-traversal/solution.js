/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var constructFromPrePost = function(preorder, postorder) {
    let pre_i = 1;
    let post_i = 0;
    const root = new TreeNode(preorder[0]);
    
    const stack = [root];
    while(pre_i < preorder.length){
        const next_val = preorder[pre_i];
        const current_node = stack[stack.length - 1];
        const next_node = new TreeNode(next_val);
        
        if(current_node.left === null){
            current_node.left = next_node
        }else{
            current_node.right = next_node
        }

        stack.push(next_node);
        while(post_i < postorder.length && stack[stack.length - 1].val === postorder[post_i]){
            post_i += 1;
            stack.pop()
        }
        pre_i += 1;
    }

    return root;    
    
};
