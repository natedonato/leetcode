/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @return {TreeNode}
 */
var bstFromPreorder = function(preorder) {
    let root = new TreeNode(preorder[0]);
    
    for(let i = 1; i < preorder.length; i++){
        let nextnode = new TreeNode(preorder[i]);
        let node = root;

        while((node.left && nextnode.val < node.val) || (node.right && nextnode.val > node.val)){
            
            if(nextnode.val < node.val){
                node = node.left
            }else{
                node = node.right
            }
            
        }
        if(nextnode.val < node.val){
                node.left = nextnode;
        }else{
                node.right = nextnode;
        }
    }

    return root;
    
};