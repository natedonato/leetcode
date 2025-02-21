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
 */
var FindElements = function(root) {
    this.vals = new Set();

    root.val = 0;

    const queue = [root];
    while(queue.length > 0){
        const next = queue.shift();
        this.vals.add(next.val);
        
        if(next.left !== null){
            next.left.val = next.val * 2 + 1
            queue.push(next.left)
        }
        
        if(next.right !== null){
            next.right.val = next.val * 2 + 2
            queue.push(next.right)
        }
    }
};

/** 
 * @param {number} target
 * @return {boolean}
 */
FindElements.prototype.find = function(target) {
    return this.vals.has(target)
};

/** 
 * Your FindElements object will be instantiated and called as such:
 * var obj = new FindElements(root)
 * var param_1 = obj.find(target)
 */
