/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {string} traversal
 * @return {TreeNode}
 */
var recoverFromPreorder = function(traversal) {
    let j = 0;
    let rootVal = ""
    while(traversal[j] !== "-" && j < traversal.length){
        rootVal += traversal[j]
        j++;
    }
    
    const root = new TreeNode(parseInt(rootVal));
    let stack = [root];
    let depth = 0;
    
    for(let i = j; i < traversal.length; i++){
        let nextDepth = 0;
        while(traversal[i] === '-'){
            nextDepth += 1;
            i += 1;
        }
        let nextVal = ""
        while(i < traversal.length && traversal[i + 1] !== "-"){
            nextVal += traversal[i]
            i += 1;
        }
        nextVal += traversal[i]
        const nextNode = new TreeNode(parseInt(nextVal));
        
        let last = stack.pop();        
        
        while(depth >= nextDepth){
            last = stack.pop();
            depth -= 1;
        }
    
        if(!last.left){
            last.left = nextNode;
        }else{
            last.right = nextNode;
        }
        
        stack.push(last);
        stack.push(nextNode);
        depth += 1;
    }
    
    return root;
};
