"""
Answer:
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
      res = None
      while head is not None :
        res = ListNode(head.val,res)
        head = head.next
      return res
"""
Tests:
"""
solution = Solution()
linkedlist1 = ListNode(1,ListNode(2,ListNode(2,ListNode(2))))
sol = solution.reverseList(linkedlist1)
while sol:
    print("val:",sol.val)
    sol = sol.next