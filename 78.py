"""
Answer :
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(n,actualset,took) :
            # On prend le set
            if n >= len(nums) :
                return
            if took :
                res.append(actualset)
            # On va du coté (prendre le nombre)
            backtrack(n+1,actualset+[nums[n]],True)
            # On va du coté (ne pas prendre le nombre)
            backtrack(n+1,actualset,False)
        backtrack(-1,[],True)
        return res