# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Head node (entry to the linked list)
        def ll_to_str(ll):

            values = []

            current_node = ll

            while current_node:
                values.append(str(current_node.val))
                current_node = current_node.next
            
            return "".join(values)
        
        #Call this on both lists
        str_l1 = ll_to_str(l1)
        reversed_l1 = str_l1[::-1]

        str_l2 = ll_to_str(l2)
        reversed_l2 = str_l2[::-1]

        reversed_l1_int = int(reversed_l1)
        reversed_l2_int = int(reversed_l2)

        reversed_result = reversed_l1_int + reversed_l2_int

        reversed_result_str = str(reversed_result)

        #Send unreversed result into a linked list
        #First loop through str, convert str[i] to num, and append to a new list
        result_list = []
        for i in reversed_result_str:
            result_list.append(int(i))
        
        l3 = None
        
        for i in result_list:
            l3 = ListNode(i, l3)

        return l3
        