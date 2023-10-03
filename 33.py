"""
Answer:
"""
class Solution:
    def search(self, nums, target):
        if len(nums) <= 2:
            if target in nums:
                return nums.index(target)
            return -1
        l,r = 0,len(nums)-1
        while r >= l :
            mid = (r+l)//2
            print("l = ",l,"r = ",r,"mid = ",mid)
            if nums[mid] == target :
                return mid
            
            if nums[mid] - nums[l] >= 0 :
                # On est monotone de gauche
                #print("monotone de gauche")
                #print("nums[mid] = ",nums[mid],"target = ",target,"nums[l] = ",nums[l])
                if nums[l] <= target and target < nums[mid]:
                    #print("target est dans la monotone de gauche")
                    r = mid - 1
                else :
                    # target n'est pas dans la monotone de gauche
                    #print("target n'est pas dans la monotone de gauche")
                    l = mid + 1
            else :
                # On est monotone de droite
                #print("monotone de droite")
                #print("nums[mid] = ",nums[mid],"target = ",target,"nums[r] = ",nums[r])
                if  nums[mid] < target and target <= nums[r] :
                    #print("target est dans la monotone de droite")
                    l = mid + 1
                else :
                    # target n'est pas dans la monotone de droite
                    #print("target n'est pas dans la monotone de droite")
                    r = mid - 1
        return -1

                

"""
Tests:
"""
solution = Solution()
"""
print(solution.search([4,5,6,7,0,1,2],0))
print(solution.search([4,5,6,7,0,1,2],3))
print(solution.search([1],0))
print(solution.search([3,1],1))
print(solution.search([1,3,5],5))
print(solution.search([5,1,3],3))
"""
print(solution.search([5,1,2,3,4],1))