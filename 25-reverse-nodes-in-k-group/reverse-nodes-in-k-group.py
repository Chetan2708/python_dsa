# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        prev = next = None
        curr = head
        count = 0

        # Check if there are at least k elements remaining
        temp = head
        for _ in range(k):
            if temp is None:
                return head  # Less than k elements remaining, no reversal needed
            temp = temp.next

        # Reverse the first k group
        while curr and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        # Recursion
        if next:
            head.next = self.reverseKGroup(next, k)

        return prev
