class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        count = 0
        self.stack.append(price)
        for i in reversed(self.stack):
            if i <= price:
                count += 1
            else:
                
                return count
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)