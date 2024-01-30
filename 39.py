"""
Answer (sympa et un peu leetcode):
"""
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def dfs(candidate, index):
            print("candidate:",candidate)
            somme_candidat = sum(candidate) if candidate != [] else 0
            if somme_candidat > target :
                return
            if somme_candidat == target :
                res.append(candidate)
                return
            for i in range(index,len(candidates)): # Permet d'eviter les doublon
                dfs(candidate + [candidates[i]] , i)
        dfs([],0)
        return res
"""  
class Solution:
    def combinationSum(self, candidates, target: int):
        ans = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):                       # try out each possible cases
            if cur_sum > target: return                   # this is the case, cur_sum will never equal to target
            if cur_sum == target: ans.append(cur); return # if equal, add to `ans`
            for i in range(idx, n): dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # DFS
        dfs([], 0, 0)
        return ans             

"""   
"""
Tests :
"""
solution = Solution()
print(solution.combinationSum([2,3,6,7],7))
print("-------------------")
print(solution.combinationSum([2,3,5],8))
print("-------------------")
print(solution.combinationSum([2],1))
print("-------------------")
print(solution.combinationSum([7,3,2],18))