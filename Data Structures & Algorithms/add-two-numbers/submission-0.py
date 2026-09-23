# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(l):
            curr, prev = l, None
            while curr:
                temp, curr.next = curr.next, prev
                prev, curr = curr, temp
            return prev
            
        def num(l):
            reverse = rev(l)
            curr = reverse
            res = []
            while curr:
                res.append(curr.val)
                curr = curr.next
            # print(res)
            return int("".join(map(str, res)))
        
        num1, num2 = num(l1), num(l2)
        res = num1 + num2
        arr = list(str(res))


        dummy = ListNode(0)
        curr = dummy

        for ch in arr:
            curr.next = ListNode(ch)
            curr = curr.next
        
        return rev(dummy.next)