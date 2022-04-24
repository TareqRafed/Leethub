# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseListToNumber(self, l1: Optional[ListNode]):
        stillNext = l1
        nums = []
        while stillNext:
            nums.insert(0, stillNext.val)
            stillNext = stillNext.next
        numbersStr = map(str, nums)
        return int(''.join(numbersStr))
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = self.reverseListToNumber(l1) + self.reverseListToNumber(l2)
        strNum = str(num)
        listNodes = []
        for node in reversed(strNum):
            listNodes.append(ListNode(node, None))
        
        ## connect the nodes
        for i in range(len(listNodes)):
            if i + 1 < len(listNodes):
                listNodes[i].next = listNodes[i+1]
        
        return listNodes[0]
            
        
        