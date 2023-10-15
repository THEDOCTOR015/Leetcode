"""
Answer (envie de pleurer):
"""
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # On met le pointeur de gauche sur le dummy node
        dummy = ListNode(0, head)
        left = dummy
        # On met le pointeur de droite sur le head
        right = head
        # On met le right au bon endroit
        while n > 0:
            right = right.next
            n -= 1
        # On avance les deux pointeurs jusqu'a la fin
        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
            
        
"""
Tests:
"""
Solution = Solution()
res = Solution.removeNthFromEnd(ListNode(1,ListNode(2)),2)
print("---")
while res :
    print(res.val)
    res = res.next

res = Solution.removeNthFromEnd(ListNode(1,ListNode(2)),1)
print("---")
while res :
    print(res.val)
    res = res.next

            
