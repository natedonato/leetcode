/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var allPossibleFBT = function(n, memo = {}) {
    
    // in base case of 1 node, return single new node
    if(n === 1){
        let root = new TreeNode(0)
        return [root];
    }
    
    if(n === 2){
        return [];
    }
    
    if(n > 2){
        if(memo[n]){
            return memo[n]
        }
        let output = [];
        // root adds a single node
        let remaining = n - 1
        
        // loop through each possible optoin
        for(let i = 1; i < remaining; i++){
            // make different possible distributions of left and right nodes
            let leftNodes = i;
            let rightNodes = remaining - i;
            
            let leftSolutions = allPossibleFBT(leftNodes, memo);
            let rightSolutions = allPossibleFBT(rightNodes, memo);
                        
            for(const leftSolution of leftSolutions){
                for(const rightSolution of rightSolutions){
                    const root = new TreeNode(0, leftSolution, rightSolution);
                    output.push(root);
                }
            }
        }   
        
        memo[n] = output;
        return output;   
    }
};
