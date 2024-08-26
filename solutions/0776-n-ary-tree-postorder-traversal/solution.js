/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var postorder = function(root) {
    if(!root){
        return [];
    }
    
    const output = [];
    
    function traverse(node){
        for(const child of node.children){
            traverse(child);   
        }
        output.push(node.val);
    }
  
    traverse(root);
    
    return(output);
};
