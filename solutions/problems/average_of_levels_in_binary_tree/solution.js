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
var averageOfLevels = function(root) {
    let output = [];
    
    let currLevel = [root];
    
    while(currLevel.length > 0){
        let nextLevel = [];
        let sum = 0;
        
        currLevel.forEach(el => {
            sum += el.val;
            
            if(el.left){
                nextLevel.push(el.left);
            };
            if(el.right){
                nextLevel.push(el.right);
            }
        });
        
        const avg = sum / currLevel.length;
        output.push(avg);
        currLevel = nextLevel;
        
    }
        
    
    
    return output;
};