/**
 * Definition for a binary tree node.
  function TreeNode(val) {
      this.val = val;
      this.left = this.right = null;
  }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */

function TreeNode(val) {
      this.val = val;
      this.left = this.right = null;
}

var sortedArrayToBST = function(nums) {
    if (!nums.length) {
        return null; 
    }

    let middleidx = Math.floor(nums.length / 2); 
    let middle = nums[middleidx];
    let left = nums.slice(0, middleidx);
    let right = nums.slice(middleidx + 1);

    let node = new TreeNode(middle);
    node.left = sortedArrayToBST(left);
    node.right = sortedArrayToBST(right);

    return node;
};