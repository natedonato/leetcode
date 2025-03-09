/**
 * @param {number[]} colors
 * @param {number} k
 * @return {number}
 */
var numberOfAlternatingGroups = function(colors, k) {
    let alternating_count = 0
    let group_count = 0
    let prev_color = colors[colors.length - 1]

    for(let i = 0; i < colors.length + k - 1; i++){
      
        const index = i % colors.length;
        const current_color = colors[index]

        if(current_color === prev_color){
            alternating_count = 1;
        }else{
            alternating_count += 1;
        }

        if(alternating_count >= k){
            group_count += 1;
        }

        prev_color = current_color
    }

    return group_count;
};
