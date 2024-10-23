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
 * @return {TreeNode}
 */
var replaceValueInTree = function(root) {
    const queue = [[root]];
    
    while(queue.length > 0){
        let sum = 0;
        let l = queue.length;
        let level = [];
        
        for(let i = 0; i < l; i++){
            const nodes = queue.shift();
            let siblingSum = 0;
            
            for(const node of nodes){
                siblingSum += node.val;
                if(node.left || node.right){
                    const next = []
                    node.left && next.push(node.left);
                    node.right && next.push(node.right);
                    queue.push(next);
                }
            }
            
            sum += siblingSum;
            
            level.push(nodes);
            level.push(siblingSum);
        }
        
        for(let i = 0; i < level.length; i+= 2){
            let row = level[i];
            let s = level[i+1];
            
            for(const node of row){
                node.val = sum - s;
            }
        }
        
    }
    
    return root;
};
