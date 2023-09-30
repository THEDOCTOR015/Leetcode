"""
Answer:
"""
class Solution:
    def largestRectangleArea(self, heights): 
        heights.append(0)
        stack = [(heights[0],0)]
        maxarea = 0
        for i in range(1, len(heights)):
            stack.append((heights[i],i))
            while stack[-2][0] > stack[-1][0] :
                lenght = i - stack[-2][1]
                maxarea = max(maxarea,lenght*stack[-2][0])
                stack[-1] = (stack[-1][0],stack[-2][1])
                stack.pop(-2)
                if len(stack) == 1:
                    break
        return maxarea


            


"""
Tests:
"""
solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3])) # 10
print(solution.largestRectangleArea([2,4])) # 4
print(solution.largestRectangleArea([2,1,2])) # 3
print(solution.largestRectangleArea([1,2,2])) # 4
print(solution.largestRectangleArea([1,2,2,1])) # 4
print(solution.largestRectangleArea([1,2,2,1,2])) # 5
print(solution.largestRectangleArea([1,2,2,1,2,1])) # 6
print(solution.largestRectangleArea([1,2,2,1,2,1,2])) # 7
print(solution.largestRectangleArea([1,2,3,4,5,6,7,8])) # 20
print(solution.largestRectangleArea([3,6,5,7,4,8,1,0])) # 20