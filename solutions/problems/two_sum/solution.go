import ()

func twoSum(nums []int, target int) []int {
    visited := map[int]int{}
    
    for idx1, el1 := range nums {
        difference := target - el1
        val, pres := visited[difference]
        if(pres){
            coords := []int{val, idx1}
            return coords
        }
        visited[el1] = idx1
    }
    return []int{}
}