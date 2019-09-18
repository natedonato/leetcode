/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string}
 */
var smallestFromLeaf = function(root) {
    let paths = getPaths(root);
    

    return paths.sort()[0];
};

var getPaths = function(root, currentPath = '', paths = []) {
    
    if(!root){return;}
    
    currentPath = numParser(root.val) + currentPath;
    if(!root.left && !root.right){
        paths.push(currentPath);
        currentPath -= numParser(root.val);
        return paths;
    }
    
    
    getPaths(root.left, currentPath, paths);
    getPaths(root.right, currentPath, paths);
    currentPath -= numParser(root.val);
    
    return paths
};

var numParser = function(num){
    return String.fromCharCode(num + 97);
}