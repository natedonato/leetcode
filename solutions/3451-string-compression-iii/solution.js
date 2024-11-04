/**
 * @param {string} word
 * @return {string}
 */
var compressedString = function(word) {
  let output = "";
  let prev = word[0];
  let count = 1;

  for(let i = 1; i < word.length; i++){
      const char = word[i]
      
      if(char === prev && count < 9){
        count += 1;
      }else{
        output += count;
        output += prev;
        prev = char;
        count = 1;
      }

  }
  output += count;
  output += prev;
  
    
  return output;
};
