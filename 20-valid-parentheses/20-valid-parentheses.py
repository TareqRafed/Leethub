class Solution:
    def isValid(self, s: str) -> bool:
        
        fail = False
        stack = []
        for char in s:
            if char == '(' or  char ==  '[' or  char ==  '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    fail = True
                    break
                lastOpenChar = stack.pop()
                if lastOpenChar == '(' and char != ')':
                    fail = True
                    break
                elif lastOpenChar == '[' and char != ']':
                    fail = True
                    break
                elif lastOpenChar == '{' and char != '}':
                    fail = True
                    break
        if len(stack) != 0:
            fail = True
        return not fail