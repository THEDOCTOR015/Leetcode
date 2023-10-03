"""
Answer (trash):
"""
class Solution:
    def minEatingSpeed(self, piles, h):
        def check(piles,k,h) :
            pile = piles.copy()
            while h >= 0 :
                if pile == [] :
                    return True
                h -= pile[0]//k if pile[0]%k == 0 else pile[0]//k + 1
                pile.pop(0)
            return False
        if len(piles) == 1 :
            return piles[0]//h if piles[0]%h == 0 else piles[0]//h + 1
        if h == len(piles) :
            return max(piles)
        mn, mx = 1 , max(piles)
        #print("mn:",mn,"mx:",mx)
        while mx >= mn :
            mid = (mx+mn)//2
            #print("mid:",mid)
            if check(piles,mid,h) :
                mx = mid-1
                res = mid
            else :
                mn = mid+1
        return res

"""
Answer (better) :
"""
class Solution:
    def minEatingSpeed(self, piles, h):
        
        left=1
        right=max(piles)

        while left<right:

            mid=(left+right)//2
            total=sum((pile//mid if pile%mid == 0 else pile//mid + 1) for pile in piles)
            #print("mid:",mid,"total:",total)

            if total>h:
                left=mid+1
            else:
                right=mid

        return left
"""
Tests:
"""
solution = Solution()
#print(solution.minEatingSpeed([3,6,7,11],8)==4)
print(solution.minEatingSpeed([1000000000,1000000000],3))
print(solution.minEatingSpeed([332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184],823855818))