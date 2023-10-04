"""
Answer:
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        iseven = (len(nums1) + len(nums2)) % 2
        print(iseven)
        half = (len(nums1) + len(nums2)) // 2
        print("half: ", half)
        #Permet de s'assurer que nums1 > half
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        print("nums1: ", nums1)
        print("nums2: ", nums2)
        r1 = int(len(nums1)/2) - 1
        r2 = half - r1 - 2
        print("r1:",r1,"r2:",r2)
        l1 = r1 + 1
        l2 = r2 + 1
        print("l1:",l1,"l2:",l2)


"""
Tests:
"""
solution = Solution()
print(solution.findMedianSortedArrays([1, 2,3,3,3,3], [3]))
#print(solution.findMedianSortedArrays([1, 3], [2]))
#print(solution.findMedianSortedArrays([1, 2], [3, 4]))
