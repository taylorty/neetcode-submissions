class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        return self.helper(s)

    def helper(self, s):
        num = 0
        curr = ""
        stack = []
        while self.i < len(s):
            char = s[self.i]
            self.i += 1
            if char.isdigit():
                if curr:
                    stack.append(curr)
                    curr = ""
                num = num * 10 + int(char)
                
            elif char == "[":
                val = self.helper(s)
                stack.append(num * val)
                num = 0
            elif char == "]":
                stack.append(curr)
                return "".join(stack)
            else:
                curr += char
                # if self.i == len(s) - 1:
                #     stack.append(curr)
        if curr:
            stack.append(curr)
        return "".join(stack)

