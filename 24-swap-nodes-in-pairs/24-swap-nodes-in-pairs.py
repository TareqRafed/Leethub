# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = ListNode(0, head)
        ans = None
        
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            if not ans:
                ans = b
            prev.next, b.next, a.next = b, a, b.next
            prev = a

        return ans if ans else head
