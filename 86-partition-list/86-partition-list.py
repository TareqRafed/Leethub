# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head:
            return
        
        theHead = head
        smaller = []
        bigger = []
        
        while theHead:
            if not theHead:
                break
            if theHead.val < x:
                smaller.append(theHead)
            else:
                bigger.append(theHead)
            
            theHead = theHead.next
            
        if len(smaller) == 0 or len(bigger) == 0:
            return head
        
        for i in range(len(smaller)):
            if i + 1 >= len(smaller):
                smaller[i].next = bigger[0]
                break
            smaller[i].next = smaller[i + 1] 
        
        for i in range(len(bigger)):
            if i + 1 >= len(bigger):
                bigger[i].next = None
                break
            bigger[i].next = bigger[i + 1] 
        
        return smaller[0]