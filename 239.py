"""
Answer :
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if len(nums) == 0 or k == 0:
            return []
        if k >= len(nums) :
            return [max(nums)]
        Deque = deque([nums[0]])
        firstwindow = nums[1:k]
        for element in firstwindow :
            top = Deque[len(Deque)-1]
            while Deque and element > top :
                Deque.pop()
                if len(Deque) == 0 :
                    break
                top = Deque[len(Deque)-1]
            Deque.append(element)
        res = [Deque[0]]
        
        for i in range(1,len(nums)-k+1) :
            candidate = nums[i+k-1]
            oldnum = nums[i-1]
            if Deque[0] == oldnum :
                Deque.popleft()
            if len(Deque) == 0 :
                Deque.append(candidate)
                res.append(candidate)
                continue
            top = Deque[len(Deque)-1]
            while Deque and candidate > top :
                Deque.pop()
                if len(Deque) == 0 :
                    break
                top = Deque[len(Deque)-1]
            Deque.append(candidate)
            res.append(Deque[0])
        return res
"""
Tests :
"""
solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)==[3,3,5,5,6,7])
print(solution.maxSlidingWindow([1],1)==[1])
print(solution.maxSlidingWindow([1,-1],1)==[1,-1])
print(solution.maxSlidingWindow([-7,-8,7,5,7,1,6,0],4)==[7,7,7,7,7])
print(solution.maxSlidingWindow([4,-2],2)==[4])
print(solution.maxSlidingWindow([1,3,1,2,0,5],3)==[3,3,2,5])