class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        # print(paths)
        stack = []
        for cur in paths:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
        return "/" + "/".join(stack)