/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
// function treeNode(val){
//     this.val = val;
//     this.children = new Array(10).fill(null);
// }

var longestCommonPrefix = function(arr1, arr2) {
    const trie = new Array(10);
  
    const addToTrie = (str) => {
        let node = trie;
        for(const char of str){
            const digit = parseInt(char);
            if(node[digit] === undefined){
                node[digit] = new Array(10);
            }
            node = node[digit];
        }
    }
    
    const matchPrefix = (str) => {
        let length = 0;
        let node = trie;
        let i = 0;

        while(i < str.length){
            const digit = parseInt(str[i]);
            if(node[digit] !== undefined){
                console.log("in trie")
                length += 1;
                node = node[digit]
                i += 1;
            }else{
                break;
            }
        }
        return length;
    }
    
    for(const el of arr1){
        addToTrie(el.toString())
    };

    let max = 0;
    for(const el of arr2){
        max = Math.max(matchPrefix(el.toString()), max);
    }
        
    return max;
};

