# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        nextHeadOne = list1
        nextHeadTwo = list2
        
        headList = []
        
        while nextHeadOne or nextHeadTwo:
            if nextHeadOne and not nextHeadTwo:
                headList.append(nextHeadOne)
                if nextHeadOne:
                    nextHeadOne = nextHeadOne.next
            elif nextHeadTwo and not nextHeadOne:
                headList.append(nextHeadTwo)
                if nextHeadTwo:
                    nextHeadTwo = nextHeadTwo.next
            elif nextHeadOne.val >= nextHeadTwo.val:
                headList.append(nextHeadTwo)
                if nextHeadTwo:
                    nextHeadTwo = nextHeadTwo.next
            elif nextHeadTwo.val >= nextHeadOne.val:
                headList.append(nextHeadOne)
                if nextHeadOne:
                    nextHeadOne = nextHeadOne.next
            
            
        
        for ind in range(len(headList)):
            if ind + 1 < len(headList):
                headList[ind].next = headList[ind + 1]
            else:
                headList[ind].next = None
        if len(headList) > 0:
            
            return headList[0]
        else:
            return ListNode().next