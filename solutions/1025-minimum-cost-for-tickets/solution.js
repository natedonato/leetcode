/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    const travel = new Set(days);

    const memo = new Map();

    return solve(0);

    function solve(day){
        if(memo.has(day)){
            return memo.get(day);
        }

        if(day > 365){
            return 0;
        }

        let ans;

        if(!travel.has(day)){
            ans = solve(day + 1)
        }else{
            ans = Math.min(costs[0] + solve(day + 1), costs[1] + solve(day + 7), costs[2] + solve(day + 30))
        }

        memo.set(day, ans);

        return ans;
    }
};
