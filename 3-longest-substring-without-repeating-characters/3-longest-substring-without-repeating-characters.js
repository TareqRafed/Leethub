/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let que = [];
    let longest = '';
    
    for(let i = 0; i < s.length; i++) {
        if(que.includes(s[i])) {
            console.log(que)
            if(que.length > longest.length) {
                longest = que.join('')
            }
            while(que.includes(s[i])) {
                que.shift()
            }
            que.push(s[i])
        } else {
            que.push(s[i])    
        }
    }
    if(que.length > longest.length) {
        longest = que.join('')
    }
    
    
    return longest.length
};