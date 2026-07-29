class Twitter:

    def __init__(self):
        self.feed = []
        self.follow_graph = {}

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.feed.append({'user_id': userId, 'tweet_id': tweetId})
        return None

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        if userId in self.follow_graph:
            followed = self.follow_graph[userId]
            followed.add(userId)
        else:
            followed = set([userId])
        i = len(self.feed) - 1
        while len(news) < 10 and i >= 0:
            #u = self.feed[i]['user_id']
            #u = self.feed[i]['tweet_id']
            if self.feed[i]['user_id'] in followed:
                news.append(self.feed[i]['tweet_id'])
            i -= 1
        return news

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
