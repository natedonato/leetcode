/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let currently_seen_characters = {};
    let max = 0;
    let left_idx = 0;
    
    
    // keeping track of our left side pointer, iterate through string character by character
    for(let i = 0; i < s.length; i++){
        let next_char = s.charAt(i);
        
        // if a character is unseen, mark it as seen and test our max length
        if(currently_seen_characters[next_char] != true){
            currently_seen_characters[next_char] = true;
            max = Math.max(max, i - left_idx + 1);
        }else{
            
            // if a character is seen, increase our left pointer until it hits the previously seen character;
            
            let left_char = s.charAt(left_idx)
            
            while(left_char !== next_char){
                // unset characters that are outside our moving leftmost boundary   
                currently_seen_characters[left_char] = false;
                left_idx += 1;
                left_char = s.charAt(left_idx)
            }
            
            // move left pointer past the previously seen character
            left_idx += 1;
            currently_seen_characters[next_char] = true;
        }
    }
    
    
    
    return max;
};