"""
Answer:
"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        submap = Counter(s1)
        dephasage = 0
        candidate = s2[dephasage:dephasage+len(s1)]
        for i in range(len(s2)-len(s1)+1) :
            if submap == Counter(candidate) :
                return True
            dephasage += 1
            candidate = s2[dephasage:dephasage+len(s1)]
        return False



"""
Tests:
"""
solution = Solution()
print(solution.checkInclusion("ab","eidbaooo")==True)
print(solution.checkInclusion("ab","eidboaoo")==False)
print(solution.checkInclusion("zz","dcda")==False)
print(solution.checkInclusion("adcc","dcda")==False)
print(solution.checkInclusion("hello","ooolleoooleh")==False)
print(solution.checkInclusion("ky","ainwkckifykxlribaypk")==True)
