class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = max(weights)
        e = sum(weights)
        def canShip(weight):
            daysNeed = 0
            prev = 0
            for wei in weights:
                if prev + wei <= weight:
                    prev += wei
                else:
                    daysNeed += 1
                    prev = wei
            if prev:
                daysNeed += 1
            return daysNeed <= days

        while s < e:
            m = (e - s) // 2 + s
            # print(m)
            # print(canShip(m))
            if canShip(m):
                e = m
            else:
                s = m + 1
        return s


    