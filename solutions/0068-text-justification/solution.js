/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    let lines = [];
    
    let currentLine = [];
    let currentWidth = 0;
    while(words.length > 0){
        let nextLength = words[0].length;
        
        //If current line is empty, add the next word with no spaces (guaranteed to fit)
        if(currentWidth === 0){
            currentWidth += nextLength
            currentLine.push(words.shift());
            continue;
        }else{
        
            // if current line not empty, test if next word +1 extra space char can fit
            if(currentWidth + 1 + nextLength <= maxWidth){
                
                // if it can fit, add the word  to the current line
                currentLine.push(words.shift());
                // add word width plus 1 extra char (space) to current line width
                currentWidth += 1 + nextLength;
            
            }else{
                // if it doesn't fit, start the next line
                lines.push(currentLine);
                currentLine = [];
                currentWidth = 0;
            }
        }
    }

    // if any leftover, finish the last line.
    if(currentLine.length > 0){
        lines.push(currentLine);
    }
    
    // console.log(lines);
    
    let output = [];
    
    for(let i = 0; i < lines.length; i++){
        let line = lines[i];

        // if single word line or last line, justify left.
        if(line.length === 1 || i === lines.length - 1){
            line = line.join(" ");
            while(line.length < maxWidth){
                line += " ";
            }
            output.push(line)
        }else{
        
        // if multi word, add spaces left to right
            let numGaps = line.length - 1;
            
            let numSpaces = maxWidth - line.join("").length;   
            
            let gaps = new Array(numGaps).fill("");
            
            let i = 0;
            while(numSpaces > 0){
                gaps[i % gaps.length] += " "
                numSpaces--;
                i++;
            }
            
            let str = line.shift();
            while(line.length > 0){
                str += gaps.shift();
                str += line.shift();
            }
            
            output.push(str);
        }
    }
    
    
    return output;
};
