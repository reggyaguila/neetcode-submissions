# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # anchor node, never moves, holds no real digit
        current = dummy      # pointer that walks forward, builds the list
        carry = 0

        while l1 or l2 or carry:
            sum_ll = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            digit = sum_ll % 10
            carry = sum_ll // 10

            current.next = ListNode(digit)   # attach new node after current
            current = current.next           # move current forward to it

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next   # skip the dummy, return the real head
        