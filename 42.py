"""
Answer (not complete):
"""
class Solution:
    def trap(self, height):
        spikes = []
        for index in range(len(height)):
            if index == 0 :
                if height[index] >= height[index+1] :
                    spikes.append((height[index],index))
                    continue
            if index == len(height)-1 :
                if height[index] >= height[index-1] :
                    spikes.append((height[index],index))
                    continue
            if height[index] >= height[index-1] and height[index] >= height[index+1] :
                spikes.append((height[index],index))
        print(spikes)
        water = 0
        for i in range(len(spikes)-1):
            gap = (spikes[i+1][1]-spikes[i][1])-1
            #print("gap:",gap)
            if gap == 0 :
                continue
            blocks = sum(height[spikes[i][1]+1:spikes[i+1][1]])
            #print("cutedheight:",height[spikes[i][1]+1:spikes[i+1][1]])
            #print("blocks:",blocks)
            addwater = min(spikes[i][0],spikes[i+1][0])*gap - blocks
            #print("addwater:",addwater)
            water += addwater
            #print("---------")
        return water


"""
Tests:
"""
solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])==6)
print(solution.trap([4,2,0,3,2,5])==9)
#print(solution.trap([4,2,3])==1)
#print(solution.trap([5,4,1,2])==1)
#print(solution.trap([5,2,1,2,1,5])==14)