/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countCompleteComponents = function(n, edges) {
    // make graph
    /// include edge count on each node
    
    // take a node
    /// BFS to find connected components
    //// use edge count to check if complete

    const graph = {}
    for(let i = 0; i < n; i++){
        graph[i] = {
            edge_count: 0,
            children: []
        }
    }

    for(const edge of edges){
        const [n1, n2] = edge

        graph[n1].edge_count += 1
        graph[n2].edge_count += 1
        graph[n1].children.push(n2)
        graph[n2].children.push(n1)
    }
    const visited = new Set();
    let complete_count = 0

    for(let node_val of Object.keys(graph)){
        node_val = parseInt(node_val)
        if(visited.has(node_val)){
            continue;
        }
        const node = graph[node_val]

        const component_edge_count = node.edge_count
        let component_node_count = 0
        const queue = [node_val]
        let complete = true;
        visited.add(node_val)

        while(queue.length > 0){
            const next_val = queue.shift();
            const next = graph[next_val]
            if(next.edge_count !== component_edge_count){
                complete = false
            }

            component_node_count += 1

            for(const child of next.children){
                if(!visited.has(child)){
                    visited.add(child)
                    queue.push(child)
                }
            }
        }

        if(component_node_count !== component_edge_count + 1){
            complete = false
        }

        if(complete){
            complete_count += 1
        }
    }

    return complete_count
};
