var ListNode= function(next, prev, count) {
    this.next = next || null;
    this.prev = prev || null;
    this.count = count || 0;
    this.items = new Set();
    this.get = () => this.items[Symbol.iterator]().next().value
    this.print = () => console.log(` count: ${this.count}, next: ${this.next ? this.next.count : "null"}, prev: ${this.prev ? this.prev.count : "null"}, items: ${[...this.items.keys()].join(",")}` )
}

var AllOne = function() {
    this.head = new ListNode(null, null,-1);
    
    this.tail = new ListNode(null,this.head,Infinity);
    this.head.next = this.tail;
    this.tail.prev = this.head;
    
    this.head.items.add("");
    this.tail.items.add("");
    this.map = new Map();
};

/** 
 * @param {string} key
 * @return {void}
 */
AllOne.prototype.inc = function(key) {
    let node = this.map.get(key);
    // console.log("\nincrementing", key);

    
    if(node === undefined){
        // console.log("no existing key, creating node")
        if(this.head.next.count === 1){
            node = this.head.next;
        }else{
            node = new ListNode(this.head.next, this.head, 1);
            node.next.prev = node;
            this.head.next = node;
        }
        node.items.add(key);
        this.map.set(key, node);
    }else{
        node.items.delete(key);
        let nextNode;
        
        if(node.next.count === node.count+1){
            nextNode = node.next;
            // console.log('using precon next node');
  
        }else{
            // console.log("making a new node:");
            nextNode = new ListNode(node.next, node, node.count + 1);
            node.next = nextNode;
            nextNode.next.prev = nextNode;
        }
        
        nextNode.items.add(key);
        this.map.set(key, node.next);
        
        if(node.items.size === 0){
            console.log('removing old empty node:');
            // node.print();
            
            node.prev.next = node.next;
            node.next.prev = node.prev;
            nextNode.prev = node.prev;
        }
    }
    
//     console.log("most recently added node: ")
//     this.map.get(key).print();
    
//     console.log("\n full list:")
//     let p = this.head;
//     while(p){
//         p.print();
//         p = p.next;
//     }
};

/** 
 * @param {string} key
 * @return {void}
 */
AllOne.prototype.dec = function(key) {
    // console.log("\ndecrementing", key)
    let node = this.map.get(key);
    let prevNode;

    node.items.delete(key);
    
    if(node.prev.count === node.count - 1 || node.count === 1){
        prevNode = node.prev;
    }else{
        // insert new node
        prevNode = new ListNode(node, node.prev, node.count - 1)
        node.prev.next = prevNode;
        node.prev = prevNode;
    }
    
    if(node.count !== 1){
        prevNode.items.add(key);    
    }
    if(node.items.size === 0){
        prevNode.next = node.next;
        node.next.prev = prevNode;
    }
    
    
    this.map.set(key, prevNode)
    
    // console.log("\n full list:")
    // let p = this.head;
    // while(p){
    //     p.print();
    //     p = p.next;
    // }
};

/**
 * @return {string}
 */
AllOne.prototype.getMaxKey = function() {
    return this.tail.prev.get();
};

/**
 * @return {string}
 */
AllOne.prototype.getMinKey = function() {
    return this.head.next.get()
};

/** 
 * Your AllOne object will be instantiated and called as such:
 * var obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * var param_3 = obj.getMaxKey()
 * var param_4 = obj.getMinKey()
 */
