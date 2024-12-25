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
 * @return {number[]}
 */
var largestValues = function(root) {
    const output = []
    const queue = [root];
    
    while(queue.length > 0){
        const s = queue.length;
        let max;
        for(let i = 0; i < s; i++){
            const node = queue.shift();
            if(node === null){
                continue;
            }
            
            if(max === undefined || node.val > max){
                max = node.val
            }
            if(node.left){
                queue.push(node.left);
            }
            if(node.right){
                queue.push(node.right);
            }
            
        }
        
        if(max !== undefined){
            output.push(max)
        }
    }
    
    return output;
};
