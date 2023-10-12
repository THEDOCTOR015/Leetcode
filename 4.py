"""
Answer:
"""
import statistics as stat
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        newarr =nums1 + nums2
        newarr.sort()
        print(newarr)
        if len(newarr)% 2 == 0 :
            print(newarr[(len(newarr)//2)])
            print(newarr[(len(newarr)//2)-1])
            return stat.mean(newarr[len(newarr)//2-1:len(newarr)//2+1])
        return newarr[(len(newarr)//2)]
"""
Tests:
"""
solution = Solution()
print(solution.findMedianSortedArrays([1,2,3,3,3,3], [3]))
#print(solution.findMedianSortedArrays([1, 3], [2]))
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
