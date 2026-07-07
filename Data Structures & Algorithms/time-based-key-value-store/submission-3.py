from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.dict = defaultdict(SortedDict)
        self.keyStore = {}  # key : list of [val, timestamp]


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key][timestamp] = value

        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # if key not in self.dict:
        #     return ""

        # timestamps = self.dict[key]
        # idx = timestamps.bisect_right(timestamp) - 1

        # if idx >= 0:
        #     closest_time = timestamps.keys()[idx]
        #     return timestamps[closest_time]
        # return ""

        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res