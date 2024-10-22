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
 * @param {number} k
 * @return {number}
 */
var kthLargestLevelSum = function(root, k) {
    const queue = [root];
    const levelSums = [];
    
    while(queue.length > 0){
        const l = queue.length;
        let sum = 0;
        
        for(let i = 0; i < l; i++){
            const node = queue.shift();
            sum += node.val;
            
            if(node.left){
                queue.push(node.left);
            }
            if(node.right){
                queue.push(node.right);
            }
        }
        levelSums.push(sum);
    }
    
    if(levelSums.length < k){
        return -1;
    }
    
    return levelSums.sort((a,b) => b-a)[k-1];
};
