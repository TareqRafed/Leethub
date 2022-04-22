/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    
    // keep adding options to tree till both right and left are null
    
    let ans = []
    let stack = []
    
    const getParen = (leftlen, rightLen) => {
        if(leftlen === n && rightLen === n) {
            const finalParen = stack.join('') 
            ans.push(finalParen)
            return
        }
        if(leftlen < n) {
            stack.push('(')
            getParen(leftlen + 1, rightLen)
            stack.pop()
        }
        
        if(rightLen < leftlen) {
            stack.push(')')
            getParen(leftlen, rightLen +1)
            stack.pop()
        }
        
    }
    getParen(0, 0)
    return ans
    
};