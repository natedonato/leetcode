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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    let output = [];

    const queue = [root];

    while(queue.length > 0){

        let row = []
        for(let i = queue.length; i > 0; i--){
            const node = queue.shift();
            if(node === null){
                continue
            }
            row.push(node.val);
            queue.push(node.left);
            queue.push(node.right);
        }


        if(row.length > 0){
            output.push(row);
        }
    }

    return output;
};
