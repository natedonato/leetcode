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
var reverseOddLevels = function(root) {
    let depth = 0;
    const queue = [root];
    
    while(queue.length > 0){
        const size = queue.length;
        depth += 1;
        
        const level = [];
        for(let i = 0; i < size; i++){
            const node = queue.shift();
            level.push(node);
            
            if(node.left){
                queue.push(node.left)
                queue.push(node.right)
            }
        }
        
        if(depth % 2 === 0){
            for(let i = 0; i < level.length / 2; i++){
                const n1 = level[i]
                const n2 = level[level.length - 1 - i];
                const temp = n1.val
                n1.val = n2.val
                n2.val = temp            
            }
        }   
    }
    
    return root
};
