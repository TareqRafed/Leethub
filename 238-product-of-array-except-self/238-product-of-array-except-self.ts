function productExceptSelf(nums: number[]): number[] {
    let prefix: number[] = []
    let postfix: number[] = []
    let tempProduct: number = 1
    let ans: number[] = [];
    for(let i = 0; i < nums.length; i++) {
        tempProduct *= nums[i]
        prefix.push(tempProduct)
    }
    tempProduct = 1;
    for(let i = nums.length - 1; i >= 0; i--) {
        tempProduct *= nums[i]
        postfix.unshift(tempProduct)
    }
    for(let i = 0; i < nums.length; i++) {
        let prefixNum = i == 0 ? 1 : prefix[i - 1]
        let postfixNum = i == nums.length - 1 ? 1 : postfix[i + 1]
        ans.push(prefixNum * postfixNum)
    }
    
    return ans
};