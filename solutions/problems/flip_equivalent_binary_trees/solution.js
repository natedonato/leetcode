/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var flipEquiv = function(root1, root2) {
    if(!root1 && !root2){
        return true
    }else if(!root1 || !root2 || root1.val !== root2.val){
        return false
    };
    
    let queue = [[root1, root2]];
    
    while(queue.length > 0){
        let [node1, node2] = queue.shift();
        
        if(checkNodes(node1, node2)){
            if(node1.left){
                queue.push([node1.left, node2.left])
            }if(node1.right){
                queue.push([node1.right, node2.right])
            }
        }else if(checkNodes(node1, flipNode(node2))){
            if(node1.left){
                queue.push([node1.left, node2.left])
            }if(node1.right){
                queue.push([node1.right, node2.right])   
            }  
        }
        else{
            return false
        }
    }
    return true
        
}

var checkNodes = function(node1, node2){

    if(node1.left){
        if(!node2.left){
            return false
        }else if(node2.left.val !== node1.left.val){
            return false
        };
        
    }else if(node2.left){
        return false;
    }
    
    if(node1.right){
        if(!node2.right){
            return false
        }else if(node2.right.val !== node1.right.val){
            return false
        }
        
    }else if(node2.right){
        return false
    }
    return true
}




var flipNode = function(node) {
    [node.left, node.right] = [node.right, node.left]
    return node
}