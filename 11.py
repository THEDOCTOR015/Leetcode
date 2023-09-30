"""
Answer:
"""
class Solution:
    def maxArea(self, height):
        maxarea = 0
        indexleft = 0
        indexright = len(height)-1
        while indexright - indexleft != 0 :
            lenght = indexright - indexleft
            maxarea = max(maxarea,min(height[indexright],height[indexleft])*lenght)
            if height[indexleft] > height[indexright] :
                indexright -= 1
            else :
                indexleft += 1
        return maxarea


"""
Tests:
"""
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])==49)
print(solution.maxArea([1,1])==1)
print(solution.maxArea([4,3,2,1,4])==16)
print(solution.maxArea([1,2,1])==2)
print(solution.maxArea([1,2,4,3])==4)