/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    if(!lists.length) return new ListNode(null, null).next
    const mergedList = new ListNode()
    const temp = []
    
    // to array
    for(let i = 0; i < lists.length; i++) {
        if(
            lists[i] !== null
        ) {
            let hasNext = lists[i]?.next;
        let currentVal = lists[i]?.val
        temp.push(currentVal)
        while(hasNext) {
            currentVal = hasNext?.val
            temp.push(currentVal)
            hasNext = hasNext.next
        }
            }
    }
    
    if(temp.length === 0) return new ListNode(null, null).next
    
    // sorting
    const sorted = temp.sort((a, b) => a-b)
    
    // to linked list
    const listNodeRef = []
    
    for(let i = 0; i < sorted.length; i++) {
        listNodeRef.push(new ListNode(sorted[i]))
    }
    
    for(let i = 0; i < listNodeRef.length; i++) {
        if(i + 1 < listNodeRef.length) {
            listNodeRef[i].next = listNodeRef[i + 1]
        }
        
    }
    return listNodeRef[0]
};