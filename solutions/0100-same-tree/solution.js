/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    let queueA = [p];
    let queueB = [q];

    while(queueA.length > 0 && queueB.length > 0){
        let c1 = queueA.shift();
        let c2 = queueB.shift();

        // if both null continue
        if(c1 === null && c2 === null){
            continue;
        }

        // if just one null return false
        if(c1 === null || c2 === null){
            return false;
        }

        // if values not equual return false
        if(c1.val !== c2.val){
            return false;
        }

        queueA.push(c1.left);
        queueA.push(c1.right);
        queueB.push(c2.left);
        queueB.push(c2.right);
    }


    return true;
};
