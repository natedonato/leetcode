/**
 * @param {string[]} folder
 * @return {string[]}
 */
function Node(){
    this.end = false;
    this.children = {};
}

var removeSubfolders = function(folder) {
    let root = new Node();
    
    for(const f of folder){
        const dirs = f.split("/");
        let current = root;
        
        for(let i = 1; i < dirs.length; i++){
            
            if(current.end === true){
                break;
            }
            
            if(current.children[dirs[i]]){
                current = current.children[dirs[i]]
            }else{
                let node = new Node();
                current.children[dirs[i]] = node;
                current = node;            
            }
        }
        
        current.end = true;
    }
        
    const output = [];
    
    for(const f of folder){
        const dirs = f.split("/");
        let current = root;
        let i = 1;
        
        while(i < dirs.length){
            if(current.end === true){
                break;
            }
            current = current.children[dirs[i]];
        
            i += 1;
        }
        
        if(i === dirs.length){
            output.push(f);
        }
        
    }
    
    return output;
};
