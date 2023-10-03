"""
Answer:
"""
class Solution:
    def findMin(self, nums):
        l , r = 0 , len(nums)-1
        guest = nums[l]
        while r >= l :
            mid = (l+r)//2
            if nums[mid] >= guest :
                l = mid +1
            else :
                guest = nums[mid]
                r = mid - 1
        return guest



"""
Tests:
"""
solution = Solution()
print(solution.findMin([4,5,6,7,0,1,2]))
print(solution.findMin([2,1]))
print(solution.findMin([2,3,4,5,1]))