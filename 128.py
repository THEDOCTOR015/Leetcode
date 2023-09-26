"""
Answer:
"""
class Solution:
    def longestConsecutive(self, nums):
        uniques = set(nums)
        max_length = 0

        while uniques:
            low = high = uniques.pop()
            
            while low - 1 in uniques or high + 1 in uniques:
                if low - 1 in uniques:
                    uniques.remove(low - 1)
                    low -= 1
                
                if high + 1 in uniques:
                    uniques.remove(high + 1)
                    high += 1

            max_length = max(high - low + 1, max_length)

        return max_length
"""
Tests:
"""
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive([0, -1]))
print(solution.longestConsecutive([1, 2, 0, 1]))