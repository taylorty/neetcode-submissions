class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        res = 0
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                s.append(int(token))
                # print(int(token))
            else:
                a = s.pop()
                b = s.pop()
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = b - a
                elif token == '*':
                    res = a * b
                elif token == '/':
                    res = int(b / a)
                s.append(res)
        return sum(s)