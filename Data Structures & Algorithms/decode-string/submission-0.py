class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        return self.helper(s)

    def helper(self, s):
        num = 0
        curr = ""
        stack = []
        while self.i < len(s):
            print(self.i)
            print(stack)
            char = s[self.i]
            if s[self.i].isdigit():
                if curr:
                    stack.append(curr)
                    curr = ""
                num = num * 10 + int(char)
                self.i += 1
            elif char == "[":
                self.i += 1
                val = self.helper(s)
                print("here")
                print(val)
                stack.append(num * val)
                num = 0
            elif char == "]":
                self.i += 1
                stack.append(curr)
                return "".join(stack)
            else:
                curr += char
                if self.i == len(s) - 1:
                    stack.append(curr)
                self.i += 1
        return "".join(stack)

