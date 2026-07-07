class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        # self.curr_min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            new_min = val
        else:
            new_min = min(val, self.min_stack[-1])
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
