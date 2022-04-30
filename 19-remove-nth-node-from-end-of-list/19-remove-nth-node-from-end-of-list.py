# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next is None:
            return None
        
        newHead = head
        listOfNode = []
        while newHead is not None:
            listOfNode.append(newHead)
            newHead = newHead.next
            
            if newHead is None:
                if n == len(listOfNode):
                    listOfNode[0] = listOfNode[1]
                    break
                listOfNode[-(n + 1)].next = listOfNode[-(n - 1)] if n > 1 else None
                
        
        return listOfNode[0]