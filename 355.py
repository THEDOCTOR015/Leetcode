"""
Answer (chelou) :
"""
import heapq
from collections import deque, defaultdict
import itertools
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(lambda: deque(maxlen=10)) # { 1 : deque(6,5,...) 2 : deque(7,4) }
        self.follows = defaultdict(lambda: set()) # { 1: set(2) }
        self.timer = itertools.count(step=-1)
        
    def postTweet(self, userId: int, tweetId: int) -> None: # O(1)
        self.tweets[userId].appendleft((next(self.timer),tweetId))

    def getNewsFeed(self, userId: int) -> List[int]: # O(1)
        tweets = list(heapq.merge(*(self.tweets[follow] for follow in self.follows[userId] | {userId}))) # | est le symbole "union"
        return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

"""
Tests:
"""