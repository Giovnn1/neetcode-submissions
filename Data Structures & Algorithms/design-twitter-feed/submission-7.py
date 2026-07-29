class Twitter:

    def __init__(self):
        self.feed = {}
        self.follow_graph = {}
        self.tot_tweet = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tot_tweet += 1
        if userId not in self.feed:
            self.feed[userId] = [[- self.tot_tweet, tweetId]]
        else:
            self.feed[userId] += [[- self.tot_tweet, tweetId]]

        return None

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        if userId in self.follow_graph:
            f = self.follow_graph[userId]
        else: 
            f = set([])
        follows = f.copy()
        follows.add(userId)

        for user in follows:
            if user in self.feed:
                tweets += self.feed[user]
        import heapq
        heapq.heapify(tweets)


        news = []
        if not tweets:
            return news

        for _ in range(10):
            tweet = heapq.heappop(tweets)
            news.append(tweet)
            if not tweets:
                return [tweet[1] for tweet in news]

        return [tweet[1] for tweet in news]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_graph:
            self.follow_graph[followerId].add(followeeId)
        else:
            self.follow_graph[followerId] = set([followeeId])
        return None

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_graph:
            self.follow_graph[followerId].discard(followeeId)
        return None
