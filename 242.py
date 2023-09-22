"""
Answer :
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        def samedict(dict1,dict2) :
            return sorted(dict1.items()) == sorted(dict2.items())

        def stringtodict(string) :
            res = {}
            for element in string :
                if element in res.keys() :
                    res[element] += 1
                else :
                    res[element] = 1
            return res
        
        dictS = stringtodict(s)
        dictT = stringtodict(t)
        return samedict(dictS,dictT)

"""
Tests :
"""
solution = Solution()
print(solution.isAnagram("anagram","nagaram"))
print(solution.isAnagram("rat","car"))