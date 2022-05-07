function threeSumClosest(nums: number[], target: number): number {
    
    let closestNumber: number = nums[0] + nums[1] + nums[nums.length - 1]
    const isClosest = (num: number) : boolean => {
            return Math.abs(num - target) < Math.abs(closestNumber - target)   
        }

    const sortedNums: number[] = nums.sort((a, b) => a - b)

    for(let i = 0; i < nums.length - 2; i++) {
        let l = i+1
        let r = nums.length - 1
        while(l < r) {
            const currentSum = sortedNums[i] + sortedNums[l] + sortedNums[r]
            if(currentSum > target) {
                r -= 1
            } else {
                l += 1
            }
            
            if(isClosest(currentSum)) {
                closestNumber = currentSum
            }
            
        }
    }
    return closestNumber
};

