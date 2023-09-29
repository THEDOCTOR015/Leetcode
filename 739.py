"""
Answer:
"""
class Solution:
    def dailyTemperatures(self, temperatures):
        st=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            print("i=",i,"st=",st,"res=",res)
            while st and temperatures[st[-1]]<temperatures[i]:
                print("res[",st[-1],"]=",i-st[-1])
                print("st.pop()=",st[-1])
                res[st[-1]]=i-st[-1]
                st.pop()
            st.append(i)
        return res
"""
Tests:
"""
solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])==[1, 1, 4, 2, 1, 1, 0, 0])