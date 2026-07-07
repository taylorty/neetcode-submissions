class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stack2 = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack and not stack2:
                    return False
                if stack:
                    stack.pop()
                elif stack2:
                    stack2.pop()
            elif s[i] == '*':
                stack2.append(i)
        if len(stack) > len(stack2):
            return False

        while stack:
            if stack2[-1] < stack[-1]:
                return False
            stack2.pop()
            stack.pop()
            
        return True