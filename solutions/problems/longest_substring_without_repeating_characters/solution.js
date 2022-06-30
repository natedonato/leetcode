/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) { 
    if(s.length === 0){
        return 0;
    }
    
    let length = 1;    

    
    // set two pointers
    let left = 0;
    let right = 0;
    
    // set character bank
    let seenChars = {};
    
    while(right < s.length){
        let nextChar = s[right];
        
        // console.log("character", nextChar, "index", right);
        // if the character is already in our substring we hit a duplicate
        if(seenChars[nextChar] === true){
            
            
            // first take care of the length
            let subLength = right - left;
            length = Math.max(length, subLength);
            
            // advance the left pointer and remove seen chars
            while(s[left] !== nextChar){
                seenChars[s[left]] = false;
                ++left;
            } 
            ++left;
            
        }else{
        // if character isn't in the substring, catalog it and keep growing
            seenChars[nextChar] = true;
        }
        
        ++right;
            
    }
    let subLength = right - left;
    length = Math.max(length, subLength);
    
    return length;
};

