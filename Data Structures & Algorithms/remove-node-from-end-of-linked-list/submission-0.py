# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = head
        total = 0

        while count:
            total += 1
            count = count.next

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        target = total - n

        i = 0
        while i < target:
            curr = curr.next
            i += 1
        
        if curr.next:
            curr.next = curr.next.next
        
        return dummy.next
