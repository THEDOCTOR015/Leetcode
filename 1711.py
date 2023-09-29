"""
Answer :
"""
from collections import Counter
class Solution:
    def countPairs(self, deliciousness):
        map = dict(Counter(deliciousness))
        res = 0
        for element,value in map.items():
            for i in range(22):
                candidate = 2**i-element
                if candidate in map:
                    if candidate == element:
                        res += value*(value-1)
                    else:
                        res += value*map[candidate]
        return res//2 % (10**9+7)



"""
Tests:
"""
solution = Solution()
print(solution.countPairs([1,1,1,3,3,3,7])==15)
print(solution.countPairs([1,3,5,7,9])==4)
print(solution.countPairs([149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234])==12)