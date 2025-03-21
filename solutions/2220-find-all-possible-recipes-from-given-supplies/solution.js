/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function(recipes, ingredients, supplies) {
    const recipe_map = {}

    for(let i = 0; i < recipes.length; i++){
        recipe_map[recipes[i]] = ingredients[i]
    }

    supplies = new Set(supplies)

    const results = {}

    for(const recipe of recipes){
        if(results[recipe] === undefined){
            solve(recipe)
        }
    }

    return recipes.filter(el => results[el] === true)


    function solve(recipe, parents = new Set()){

        const needed = recipe_map[recipe]
        parents.add(recipe)

        for(const item of needed){
            if(parents.has(item)){
                results[recipe] = false;
                parents.delete(recipe)
                return false;
            }
            if(supplies.has(item)){
                continue
            }else if(recipe_map[item] !== undefined){
                
                if(results[item] === undefined){
                    solve(item, parents)
                }

                if(results[item] === false ){
                    results[recipe] = false
                    parents.delete(recipe)
                    return false
                }
            }else{
                results[recipe] = false
                parents.delete(recipe)
                return false
            }
        }

        results[recipe] = true
        parents.delete(recipe)
        return true
    }

};
