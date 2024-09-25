/**
 * @param {string[]} words
 * @return {number[]}
 */
function trieNode(){
    this.count = 0;
    this.children = new Array(26);
}

const A = "a".charCodeAt(0)

function idx(char){
    return char.charCodeAt(0) - A;
}

var sumPrefixScores = function(words) {
    const trie = new trieNode();
    const output = [];
    for(const word of words){
        let node = trie;
        for(const char of word){
            const index = idx(char);
            if(!node.children[index]){
                node.children[index] = new trieNode();
            }
            node = node.children[index];
            node.count += 1;
        }
    }
        
    for(const word of words){
        let node = trie;
        let sum = 0;
        for(const char of word){
            const index = idx(char);
            node = node.children[index];
            sum += node.count;
        }
        output.push(sum);
    }
    
    return output;
};
