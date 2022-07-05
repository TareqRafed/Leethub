# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not k:
            return head
        
        length = 1
        last = head
        
        while last.next:
            last = last.next
            length += 1
        
        rotateTimes = k % length
        
        if not rotateTimes:
            return head
        
        last.next = head ## cycle
        
        fir = last
        sec = head
        cycle = length - rotateTimes
        while cycle:
            fir = sec
            sec = fir.next
            cycle-=1
        
        fir.next = None
        
        
        return sec
        

