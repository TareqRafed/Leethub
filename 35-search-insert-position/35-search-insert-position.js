/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {

    let ans = null;
    
    if(nums[nums.length - 1] < target) return nums.length
    
    for(let i = 0; i < nums.length; i++){
        if(nums[i] >= target && nums[i - 1] < target){
            ans = i;            
        }
    }
    
    return ans
};