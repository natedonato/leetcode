/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var flipEquiv = function(root1, root2) {
    // base cases
    if(!root1 && !root2){
        return true;
    };
    
    if((!root1 || !root2) ||(root1.val !== root2.val)){
        return false
    };
    
    const q1 = [root1];
    const q2 = [root2];
    
    while(q1.length > 0){
        let node1 = q1.shift();
        let node2 = q2.shift();
        
        // if not equal, swap
        if(!eq(node1.left, node2.left))
        {
            const temp = node2.left;
            node2.left = node2.right;
            node2.right = temp;
        };
        
        if(eq(node1.left, node2.left)){
            if(node1.left !== null){
                q1.push(node1.left);
                q2.push(node2.left);    
            }
        }else{
            return false;
        }
        
        if(eq(node1.right, node2.right)){
            if(node1.right !== null){
                q1.push(node1.right);
                q2.push(node2.right);    
            }
        }else{
            return false;
        }
    }
    
    return true;    
};

function eq(n1, n2){
    if(n1 === null && n2 === null){
        return true;
    }else if(n1 === null || n2 === null){
        return false;
    }else{
        return n1.val === n2.val;
    }
}
