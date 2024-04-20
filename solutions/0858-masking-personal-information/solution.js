/**
 * @param {string} s
 * @return {string}
 */
var maskPII = function(s) {
    if(isEmail(s)){
        return maskEmail(s)
    }else{
        return maskPhone(s)
    }
};

function isEmail(s){
    if("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".includes(s[0])){
        return true
    }

    return false;
}

function maskEmail(s){
    let [name, domain] = s.split("@").map(el => el.toLowerCase()); 
    let stars = "*****"

    return name[0] + stars + name[name.length - 1] + "@" + domain
}

function maskPhone(s){
    const separators = ['+', '-', '(', ')', ' '];
    s = s.split("").filter(el => !separators.includes(el));

    let last4 = s.slice(s.length - 4).join("")
    let first = ""
    if(s.length > 10){
        first += "+"
        for(let i = 0; i < s.length - 10; i++){
            first += "*"
        }
        first += "-"
    }

    return first + "***-***-"+last4
}
