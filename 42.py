"""
Answer (not complete):
"""
import time
class Solution:
    def trap(self, height):
        spikes = []
        print(height)
        for index in range(len(height)):
            #print("spikes:",spikes)
            if index != 0 and index != len(height)-1 :
                if height[index] > height[index-1] and height[index] > height[index+1] :
                    spikes.append((height[index],index))
            elif index == 0 :
                if height[index] > height[index+1] :
                    spikes.append((height[index],index))
            elif index == len(height)-1 :
                if height[index] > height[index-1] :
                    spikes.append((height[index],index))
        print(spikes)
        truespikes = spikes.copy()
        if len(truespikes) <= 1 :
            return 0
        index = 1
        while index < len(truespikes)-1 :
            if truespikes[index][0] < truespikes[index-1][0] and truespikes[index][0] < truespikes[index+1][0] :
                truespikes.pop(index)
                index -= 1
            index += 1
        print("truespikes:",truespikes)
        spikes = truespikes.copy()
        water = 0
        for i in range(len(spikes)-1):
            gap = (spikes[i+1][1]-spikes[i][1])
            print("gap:",gap)
            if gap == 0 :
                continue
            blocks = sum(height[spikes[i][1]:spikes[i+1][1]])
            print("cutedheight:",height[spikes[i][1]:spikes[i+1][1]])
            print("blocks:",blocks)
            addwater = max(min(spikes[i][0],spikes[i+1][0])*gap - blocks,0)
            print("addwater:",addwater)
            water += addwater
            print("---------")
        return water

"""
Answer (not optimized):
"""

class Solution:
    def trap(self, height):
        def generatespikes(height):
            spikes = [(element,index) for index,element in enumerate(height)]
            # Traitement des cotés
            while spikes[1][0] >= spikes[0][0] :
                spikes.pop(0)
                if len(spikes) <= 1 :
                    return []
            while spikes[-2][0] >= spikes[-1][0] :
                spikes.pop(-1)
                if len(spikes) <= 1 :
                    return []
            # Traitement du milieu
            index = 1
            indexleft = 0
            indexright = 2
            while index < len(spikes)-1 :
                bigleft = False
                bigright = False
                #print("index:",index)
                #print("indexleft:",indexleft)
                #print("indexright:",indexright)
                #print("spikes:",spikes)
                if spikes[index][0] <= spikes[indexleft][0] :
                    bigleft = True
                    #print("spikes[indexleft][0]:",spikes[indexleft][0])
                if spikes[index][0] <= spikes[indexright][0] :
                    bigright = True
                    #print("spikes[indexright][0]:",spikes[indexright][0])
                #print("bigleft:",bigleft)
                #print("bigright:",bigright)
                if bigleft and bigright :
                    for i in range(indexleft+1,indexright):
                        #print("i:",i)
                        spikes.pop(index)
                    indexleft = index - 1
                    indexright = index + 1
                    continue
                elif bigleft and indexright==len(spikes)-1 or bigright and indexleft==0 or indexright==len(spikes)-1 and indexleft==0 :
                    index += 1
                    indexleft = index - 1
                    indexright = index + 1
                    #print("augmentation index ! index:",index)
                    continue
                if not bigleft :
                    indexleft = max(indexleft-1,0)
                if not bigright :
                    indexright = min(indexright+1,len(spikes)-1)
                #print("----------")
                #time.sleep(3)
            return spikes



             
        def generatewater(spikes):
            water = 0
            for i in range(len(spikes)-1):
                #print("i:",i)
                gap = (spikes[i+1][1]-spikes[i][1])-1
                #print("gap:",gap)
                if gap == 0 :
                    continue
                minheight = min(spikes[i][0],spikes[i+1][0])
                #print("spike1:",spikes[i])
                #print("spike2:",spikes[i+1])
                #print("minheight:",minheight)
                blocks = sum([min(minheight, element) for element in height[spikes[i][1]+1:spikes[i+1][1]]])
                #print("blocks:",blocks)
                #print("cutedheight:",[min(minheight, element) for element in height[spikes[i][1]+1:spikes[i+1][1]]])
                addwater = minheight*gap - blocks
                #print("addwater:",addwater)
                water += addwater
                #print("water:",water)
            return water
        
        if len(height) <= 2 :
            return 0
        #print("height:",height)
        spikes = generatespikes(height)
        #print("spikes:",spikes)
        if len(spikes) <= 1 :
            return 0
        water = generatewater(spikes)
        #print("water:",water)
        #print("---------")
        return water

"""
Answer (two pointers):
"""
class Solution:
    def trap(self, height):
        if len(height) <= 2 :
            return 0
        maxright = height[len(height)-1]
        indexright = len(height)-1
        maxleft = height[0]
        indexleft = 0
        water = 0
        while True :
            #print("maxright:",maxright,"indexright:",indexright,"maxleft:",maxleft,"indexleft:",indexleft)
            if maxright < maxleft :
                # Si le pointeur a droite va bouger 
                indexright -= 1
                maxright = max(maxright,height[indexright])
                water += max(0,maxright-height[indexright])
            else :
                indexleft += 1
                maxleft = max(maxleft,height[indexleft])
                water += max(0,maxleft-height[indexleft])
            if indexright-indexleft == 1 :
                break
        return water
"""
Tests:
"""
solution = Solution()
print(solution.trap([6,2,2,9,6,8,5,8,3,7,3,8,9,8,1,2,4])==37)
print(solution.trap([4,2,3])==1)
print(solution.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])==83)
print(solution.trap([5,5,1,7,1,1,5,2,7,6])==23)
print(solution.trap([0,2,0])==0)
