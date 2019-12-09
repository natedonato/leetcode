/**
 * // Definition for a Node.
 * function Node(val,neighbors) {
 *    this.val = val;
 *    this.neighbors = neighbors;
 * };
 */
/**
 * @param {Node} node
 * @return {Node}
 */


var cloneGraph = function(node, map = {}) {
    if(map[node.val]){return map[node.val]}
    
    map[node.val] = new Node(node.val, [])
    
    node.neighbors.forEach(neighbor =>{
        map[node.val].neighbors.push(cloneGraph(neighbor, map))
        
    })
    return map[node.val]
    
};