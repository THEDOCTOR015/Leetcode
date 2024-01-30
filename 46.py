class Solution:
    def permute(self, nums):
        setnums = set(nums)
        res = []
        def dfs(candidate):
            if len(candidate) >= len(nums) :
                res.append(candidate)
                return
            for element in nums :
                if element not in setnums :
                    dfs(candidate + [element])
        return res
            
        