# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        setA = set()
        setB = set()
        while headA and headB:
            if headA.val in setB:
                return headA
            if headB.val in setA:
                return headB
            if headA.val == headB.val:
                return headA
            setA.add(headA.val)
            setB.add(headB.val)
            headA = headA.next
            headB = headB.next
        if headA:
            while headA:
                if headA.val in setB:
                    return headA
                headA = headA.next
        if headB:
            while headB:
                if headB.val in setA:
                    return headB
                headB = headB.next
        if not headA and not headB:
            return None

