# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        arr = []
        newHead = head
        while newHead:
            arr.append(newHead)
            newHead = newHead.next
        
        l, r = 0, len(arr) - 1
        
        ordered = []
        while l <= r:
            if l == r:
                ordered.append(arr[l])
                break
            ordered.append(arr[l])
            ordered.append(arr[r])
            l += 1
            r -= 1
        
        for ind, val in enumerate(ordered):
            if ind + 1 == len(ordered):
                val.next = None
                return ordered[0]
            val.next = ordered[ind + 1]
         
        