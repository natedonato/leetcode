/**
 * @param {number[][]} edges
 * @param {number} bob
 * @param {number[]} amount
 * @return {number}
 */

function TreeNode(label){
    this.label = label;
    this.connections = [];
    this.cost = [];
    this.parent = null;
    this.score = 0;
}

var mostProfitablePath = function(edges, bob, amount) {
    const nodes = [];
    
    for(let i = 0; i < amount.length; i++){
        const node = new TreeNode(i);
        node.cost = amount[i];
        nodes.push(node);
    };

    for(const edge of edges){
        const n1 = nodes[edge[0]];
        const n2 = nodes[edge[1]];
        n1.connections.push(n2)
        n2.connections.push(n1)
    };

    // find bob's path
    let visited = new Set();
    visited.add(0)
    let queue = [nodes[0]];
    let best = null;

    while(queue.length > 0){
        const current = queue.shift();
        if(current.label === bob){
            break;
        }
        for(const child of current.connections){
            if(!visited.has(child.label)){
                visited.add(child.label);
                child.parent = current;
                queue.push(child);
            }
        }
    }

    visited = new Set();
    visited.add(0);
    queue = [nodes[0]];
    bob = nodes[bob];

    while(queue.length > 0){
        const l = queue.length;

        for(let i = 0; i < l; i++){
            const node = queue.shift();
            
            if(node === bob){
                node.score += node.cost / 2;
            }else{
                node.score += node.cost;
            }

            if(node.label !== 0 && node.connections.length === 1){
                if(best === null || best < node.score){
                    best = node.score;
                }
            }else{
              for(const child of node.connections){
                if(!visited.has(child.label)){
                        visited.add(child.label);
                        child.score += node.score
                        queue.push(child);
                    }
                }
            }
        }

        if(bob !== null){
            bob.cost = 0;
            bob = bob.parent;
        }
    }

    return best;
};
