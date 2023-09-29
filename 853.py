"""
Answer:
"""
class Solution:
    def carFleet(self, target: int, position, speed):
        def meet(position1,speed1,position2,speed2) :
            if speed1 == speed2 :
                if position1 == position2 :
                    return 0
                return False
            t = (position2-position1)/(speed1-speed2)
            if t >= 0 :
                return t
            return False
        if len(position) <= 1 :
            return len(position)
        stack = [(p,s) for p,s in zip(position,speed)]
        stack.sort(key=lambda x:x[0])
        indexpointeur = -1
        while True :
            if len(stack) == -(indexpointeur):
                return len(stack)
            targetposition = stack[indexpointeur-1][0]
            targetspeed = stack[indexpointeur-1][1]
            refposition = stack[indexpointeur][0]
            refspeed = stack[indexpointeur][1]
            time = meet(refposition,refspeed,targetposition,targetspeed)
            if not time :
                indexpointeur -= 1
                continue
            totalpotition = time*targetspeed + targetposition
            if totalpotition > target :
                indexpointeur -= 1
                continue
            stack.pop(indexpointeur-1)


"""
Tests:
"""
solution = Solution()
print(solution.carFleet(12,[10,8,0,5,3],[2,4,1,1,3])==3)
print(solution.carFleet(10,[6,8],[3,2])==2)
print(solution.carFleet(100,[0,2,4],[4,2,1])==1)