class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(index, currStr):
            if index == len(digits):
                res.append(currStr)
                return
            char = digits[index]
            options = digitToChar[char]
            for i in range(len(options)):
                dfs(index + 1, currStr + options[i])


        if digits:
            dfs(0, "")

        return res