class Solution:
    def isValid(self, s: str) -> bool:
        m = {"[": "]", "{": "}", "(": ")"}
        st = []
        for char in s:
            if char in m:
                st.append(m[char])
            elif char in m.values():
                if not st:
                    return False
                top = st.pop()
                if top != char:
                    return False
        # print(st)
        return not st