"""
Answer (trash):
"""
import time
class Solution:
    def twoSum(self, numbers, target):
        #print("numbers:",numbers)
        #print("target:",target)
        left = 0
        right = len(numbers)-1
        stack = []
        while left != len(numbers)-1 :
            #print("l:",left,"r:",right)
            if numbers[left] in stack :
                left += 1
                right = len(numbers)-1
                continue
            res = numbers[left]+numbers[right]
            #print("res:",res)
            if res > target :
                right -= 1
                continue
            elif res == target :
                return [left+1,right+1]
            else :
                stack.append(numbers[left])
                left += 1
                right = len(numbers)-1
            time.sleep(1)

"""
Answer (correct):
"""
class Solution:
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            s=numbers[i]+numbers[j]
            if s==target:
                return [i+1,j+1]
            if s>target:
                j-=1
            else:
                i+=1
        return []  

"""
Tests:
"""
solution = Solution()
#print(solution.twoSum([2,7,11,15],9)) 
#print(solution.twoSum([2,3,4],6)) 
#print(solution.twoSum([-1,0],-1))
#print(solution.twoSum([0,0,3,4],0))
#print(solution.twoSum([0,0,0,0],0))
print(solution.twoSum([5,25,75],100))