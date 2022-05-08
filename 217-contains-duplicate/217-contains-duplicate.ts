function containsDuplicate(nums: number[]): boolean {
    let hmap = {}
    let ans = false
    for(let i = 0; i < nums.length; i++) {
        if(hmap[nums[i]]) {
            ans = true
            break
        } else {
            hmap[nums[i]] = true
        }
    }
    
    return ans
    
};