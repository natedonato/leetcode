/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number} m
 * @param {number} n
 * @param {ListNode} head
 * @return {number[][]}
 */
var spiralMatrix = function(m, n, head) {
    const dirs = [
        [0,1],  // right
        [1,0],  // down
        [0,-1], // left
        [-1,0], // up
    ]
    
    let currentDir = 0;
    
    const output = new Array(m).fill(0).map(el => new Array(n).fill(-1));
    let p = [0,0];
    
    while(head){
        output[p[0]][p[1]] = head.val;
        head = head.next;
        let next = [p[0] + dirs[currentDir][0], p[1] + dirs[currentDir][1]];
        
        if(output[next[0]] === undefined || (output[next[0]][next[1]] !== -1)){
            currentDir += 1;
            currentDir %= 4;
        }
        
        p[0] = p[0] + dirs[currentDir][0];
        p[1] = p[1] + dirs[currentDir][1];
    }
    
    return output;
};
