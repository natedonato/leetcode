/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var countPaths = function(n, roads) {
    const nodes = new Array(n).fill(0).map((el, idx) => {
        return {
            val: idx,
            edges: [],
        }
    })
    const times_visited = new Array(n).fill(Infinity)
    const paths = new Array(n).fill(0)


    for(const edge of roads){
        const [node1, node2, time] = edge
        nodes[node1].edges.push([node2, time])
        nodes[node2].edges.push([node1, time])
    }

    let best_time = Infinity;
    times_visited[0] = 0;
    paths[0] = 1;

    const queue = new MinPriorityQueue((node) => node.time_visited);

    queue.enqueue({val: 0, time_visited: 0})

    while(!queue.isEmpty()){
        const item = queue.dequeue()
        const current_time = item.time_visited

        if(current_time > times_visited[item.val]){
            continue;
        }

        node = nodes[item.val];

        if(node.val === n-1){
            best_time = current_time
            continue;
        }

        for(const edge of node.edges){
            const next_node = nodes[edge[0]]
            const next_time = (current_time+ edge[1]);

            if(next_time < times_visited[next_node.val]){
                times_visited[next_node.val] = next_time
                paths[next_node.val] = paths[node.val]
                paths[next_node.val] %= (10 ** 9 + 7)
                queue.enqueue({val: next_node.val, time_visited: next_time});
            }else if(next_time === times_visited[next_node.val]){
                paths[next_node.val] += paths[node.val]
                paths[next_node.val] %= (10 ** 9 + 7)
            }
        }
    }

    return paths[n-1]

};

