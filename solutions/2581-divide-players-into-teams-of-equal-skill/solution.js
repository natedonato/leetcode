/**
 * @param {number[]} skill
 * @return {number}
 */
var dividePlayers = function(skill) {
    skill = skill.sort((a,b) => a - b);
    let p = skill[0] + skill[skill.length-1];
    console.log(p)
    let cs = skill[0] * skill[skill.length-1]
    
    let l = 1;
    let r = skill.length - 2;
    
    
    
    while(l < r){
        if(skill[l] + skill[r] !== p){
            return -1;
        }
        cs += skill[l] * skill[r]
        
        l++
        r--
    }
                             
    return cs;
                            
};
