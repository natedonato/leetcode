/**
 * @param {string} s
 * @return {boolean}
 */

var checkValidString = function(s) {
    s = s.split('');
    let open_parens = [];
    let stars = [];
    
    
    for(let i = 0; i < s.length; i++){
        const char = s[i];
        
        switch(char){
            case '(':
                open_parens.push(i);
                break
            case ')':
                if(open_parens.length > 0){
                    open_parens.pop();
                }else if (stars.length > 0){
                    stars.pop();
                }else{
                    return false;
                }
            break
            case '*':
                stars.push(i)
            break
        }
    }
      
    if(open_parens.length > stars.length){
        return false
    }
    
    while(open_parens.length > 0){
        let a = open_parens.pop()
        let b = stars.pop()
        if(a > b){return false;}
    }
    
    return true
};