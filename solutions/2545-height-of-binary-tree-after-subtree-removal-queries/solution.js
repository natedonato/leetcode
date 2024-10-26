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
 * @param {number[]} queries
 * @return {number[]}
 */
var treeQueries = function(root, queries) {
    // if(!root){
    //     return [];
    // }
    
    let answer = {};
    let heights = {};
    
    
    // compute max height of a node's children
    function findMaxHeight(node){
        if(!node){
            return 0
        }
        
        if(heights[node.val] === undefined){
            heights[node.val] = 1 + Math.max(findMaxHeight(node.left), findMaxHeight(node.right));
        }
        
        
        
        return heights[node.val];
    }
    
    // dfs traversal where we calculate 
    function dfs(node, currentDepth, maxDepthWithoutCurrentNode){
        if(!node){
            return 0;
        }
        
        // add max depth without a given node to the map of answers
        answer[node.val] = maxDepthWithoutCurrentNode;
        
        dfs(node.left, currentDepth + 1, Math.max(maxDepthWithoutCurrentNode, currentDepth + findMaxHeight(node.right)));
        
        dfs(node.right, currentDepth + 1, Math.max(maxDepthWithoutCurrentNode, currentDepth + findMaxHeight(node.left)));
    }
    
    dfs(root, 0, 0);
    
    return queries.map(el => answer[el]);
};
