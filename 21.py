"""
Answer (leetcode):
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

"""
Answer:
"""
class Solution:
    def mergeTwoLists(self, list1, list2):
        
"""
Tests:
"""
solution = Solution()
linkedlist1 = ListNode(1,ListNode(2,ListNode(2,ListNode(2))))
linkedlist2 = ListNode(1,ListNode(3,ListNode(4,ListNode(6))))
sol = solution.mergeTwoLists(linkedlist1,linkedlist2)
while sol:
    print("val:",sol.val)
    sol = sol.next