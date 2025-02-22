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
    let i = 0;

    let [rootVal, nextIndex] = getNextInt(0, traversal);
    i = nextIndex;

    const root = new TreeNode(rootVal);
    
    const stack = [root];

    while(i < traversal.length){
        let [depth, nextIndex] = getDepth(i, traversal);
        i = nextIndex;
        let nextIntData = getNextInt(i, traversal);
        let val = nextIntData[0]
        i = nextIntData[1];

        while(depth < stack.length){
            stack.pop();
        }

        const prevNode = stack[stack.length - 1];
        if(prevNode.left === null){
            prevNode.left = new TreeNode(val);
            stack.push(prevNode.left);
        }else{
            prevNode.right = new TreeNode(val);
            stack.push(prevNode.right);
        }
    }

    return root;
};


function getNextInt(index, traversal){
    let output = []
    
    while(traversal[index] !== "-" && index < traversal.length){
        output.push(traversal[index])
        index += 1
    }
    return [parseInt(output.join("")), index];
}

function getDepth(index, traversal){
    let depth = 0
    
    while(traversal[index] === "-"){
        depth += 1
        index += 1
    }
    return [depth, index];
}
