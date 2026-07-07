class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            curr = i
            while s[i] in "0123456789":
                i += 1
            num = int(s[curr:i])
            res.append(s[i + 1: i + 1 + num])
            i = i + 1 + num
        return res

        # return list(s.split("你"))