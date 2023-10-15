"""
Answer:
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        listres = []
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            listres.append(value%10)
            carry = value//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            listres.append(carry)
        linkedlist = ListNode(listres[-1])
        for i in range(len(listres)) :
            index = -1-i
            if index == -1:
                continue
            
            linkedlist = ListNode(listres[index], linkedlist)
            
        return linkedlist
            
                
        
"""
Tests:
"""    
