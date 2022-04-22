/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let hmap = {}
    let ans = []
    
    nums.forEach((num, index) => {
        if(hmap[num]?.value === num) {
            ans.push(hmap[num].index, index)
        } else {
            hmap[num] = {
            value: target - num,
            index,
            }    
        }
        
    })
    
    if(!ans.length) {
        nums.forEach((num, index) => {
        if(hmap[target - num]?.value === num && hmap[target - num]?.index !== index) {
            ans.push(index)
        }
    })
        
    }
    
    
    return ans

};