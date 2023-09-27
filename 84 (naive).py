"""
Answer:
"""
class Solution:
    def largestRectangleArea(self, heights):
        maxarea = 0
        for index1,element1 in enumerate(heights):
            for index2,element2 in enumerate(heights[index1:]):
                candidat = min(min(heights[index1:(index1+1)+index2]),element1) * (index2+1)
                if candidat > maxarea:
                    maxarea = candidat
        return maxarea

"""
Tests:
"""
solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3])) # return 10
print(solution.largestRectangleArea([2,4])) # return 4
print(solution.largestRectangleArea([0,1,0,1]))