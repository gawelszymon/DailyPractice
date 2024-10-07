# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to help simplify the merging process
        dummy = ListNode()
        tail = dummy  # This will be the tail of the merged list
        
        # While both lists have nodes, compare their values and merge accordingly
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Append list1 node to merged list
                list1 = list1.next  # Move to the next node in list1
            else:
                tail.next = list2  # Append list2 node to merged list
                list2 = list2.next  # Move to the next node in list2
            tail = tail.next  # Move the tail pointer forward

        # If there are remaining nodes in either list, attach them
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        # Return the merged list, which starts after the dummy node
        return dummy.next
        