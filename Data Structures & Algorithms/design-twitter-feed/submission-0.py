class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set) # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int):
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # Using negative counts for easy min-heap usage

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        # Ensure the user sees their own tweets by following themselves implicitly
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # Get the index of the most recent tweet for this followee
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # 2. Extract the 10 most recent tweets across all followees
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # If the user has older tweets, push the next one into the heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

