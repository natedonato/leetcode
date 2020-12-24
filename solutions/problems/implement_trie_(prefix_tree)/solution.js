/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.data = {};
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let obj = this.data;
    word.split('').forEach(char => {
        if(!obj[char]){
            obj[char] = {};
        }
        obj = obj[char];
    })
    obj['END'] = true;
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let obj = this.data
    for(const char of word){
        obj = obj[char];
        if(obj === undefined){
            return false;
        }
    }
    return obj['END'] === true;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let obj = this.data
    for(const char of prefix){
        obj = obj[char];
        if(obj === undefined){
            return false;
        }
    }
    return true;
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */