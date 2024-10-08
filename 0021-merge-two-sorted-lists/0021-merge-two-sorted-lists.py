# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        chain = head
        
        
        while list1 and list2:
            if list1.val < list2.val:
                chain.next = list1
                list1 = list1.next
            else:
                chain.next = list2
                list2 = list2.next
            chain = chain.next
                
        if list1:
            chain.next = list1
        elif list2:
            chain.next = list2
            
        return head.next
                    
        