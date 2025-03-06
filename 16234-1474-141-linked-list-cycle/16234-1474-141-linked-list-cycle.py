class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        val1 = head
        val2 = head

        while val2 and val2.next:
            val1 = val1.next
            val2 = val2.next.next
            if val2 == val1:
                return True

        return False        