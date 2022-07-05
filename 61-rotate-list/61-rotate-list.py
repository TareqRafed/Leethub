# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = head
        end = head
        if not head:
            return head
        length = 0
        s = head
        while s:
            s = s.next
            length += 1
        while k % length:
            start = ans
            end = ans
            beforeLast = ans
            while end.next:
                beforeLast = end
                end = end.next

            end.next = start
            beforeLast.next = None
            k -= 1
            ans = end
        
        return ans
        

