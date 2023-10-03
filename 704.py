"""
Answer:
"""
class Solution:
    def search(self, nums, target):
        min, max = 0, len(nums)-1

        while min <= max:
            print("min: ", min, "max: ", max)
            mid = (min + max) // 2
            print("mid: ", mid)
            if target < nums[mid]:
                max = mid -1
            elif target > nums[mid]:
                min = mid + 1
            else:
                return mid
        return -1
"""
Tests:
"""
solution = Solution()
print(solution.search([-1,0,3,5,8,12], 9))
#print(solution.search([-1,0,3,5,9,12], 2))
#print(solution.search([5], 4))
#print(solution.search([-1,0,3,5,9,12], 11))