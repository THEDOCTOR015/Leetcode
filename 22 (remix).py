"""
Answer :
"""

global listpackets
listpackets = []
class Solution:
    def createpackets(depth,currentpacket,goal) :
        print("currentpacket : ",currentpacket," depth : ",depth," goal : ",goal)
        if depth == goal :
            if currentpacket not in listpackets :
                listpackets.append(currentpacket)
            return
        newpacket = currentpacket.copy()
        newpacket.append(1)
        Solution.createpackets(depth+1,newpacket,goal)
        for i in range(len(currentpacket)) :
            newpacket = currentpacket.copy()
            newpacket[i] += 1
            Solution.createpackets(depth+1,newpacket,goal)

    def packetstoparenthesis(packets):
        res = ""
        for packet in packets :
            res += "("*packet + ")"*packet
        return res
    
    def generateParenthesis(self, n):
        listparenthesis = []
        Solution.createpackets(1,[1],n)
        for packets in listpackets :
            listparenthesis.append(Solution.packetstoparenthesis(packets))
        return listparenthesis

"""
Tests :
"""

print(Solution.generateParenthesis(Solution,3))