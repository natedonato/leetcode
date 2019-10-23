/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    let paths = [];
    if(!root){
        return [];
    }
    if(root.val === sum && !root.left && !root.right){
        paths.push([root.val]);
    }
    sum -= root.val;
    let path = [root.val];
    
    if(root.left){
        dfsUtil(root.left, path, sum);
    }
    if(root.right){
        dfsUtil(root.right, path, sum);
    }
    
    function dfsUtil(node, path, sum){
        if(!node){
            return;
        }
        
        sum -= node.val;
        path.push(node.val);
        
        if(sum === 0 && !node.left && !node.right){
            paths.push(path.slice(0));
        }else{
            dfsUtil(node.left, path, sum);
            dfsUtil(node.right, path, sum);
        }
        
        path.pop();
    }
    
    
    return paths;
};