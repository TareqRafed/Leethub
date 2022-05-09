function findMin(nums: number[]): number {
    if(nums.length === 1) return nums[0]
    
    const firstE: number = nums[0]
    const lastE: number = nums[nums.length - 1]
    
    const leftSide = nums.slice(0, Math.floor(nums.length / 2))
    const rightSide = nums.slice(Math.floor(nums.length / 2), nums.length)
    
    console.log(leftSide, rightSide)
    
    const middleE: number = rightSide[0]
    
    let temp: null | number = null
    
    if(rightSide[0] > rightSide[rightSide.length - 1]) {
        temp = rightSide[0]
        let i = 0
        while(temp <= rightSide[i]) {
            temp = rightSide[i]
            i+=1
        }
        temp = rightSide[i]
    } else if(leftSide[0] > leftSide[leftSide.length - 1]) {
        temp = leftSide[0]
        let i = 0
        while(temp <= leftSide[i]) {
            temp = leftSide[i]
            i+=1
        }
        temp = leftSide[i]
    } else {
        temp = Math.min(leftSide[0], rightSide[0])
    }
    
    return temp
};