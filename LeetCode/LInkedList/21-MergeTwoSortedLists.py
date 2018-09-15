# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        new_l = ListNode(0)
        head = new_l
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                new_l.val = l1.val
                l1 = l1.next
            else:
                new_l.val = l2.val
                l2 = l2.next
            new_l.next = ListNode(0)
            new_l = new_l.next
        # print listNodeToString(head)
        if l1 != None:
            while l1 != None:
                new_l.val = l1.val
                l1 = l1.next
                if l1 != None:
                    new_l.next = ListNode(0)
                    new_l = new_l.next
        if l2 != None:
            while l2 != None:
                new_l.val = l2.val
                l2 = l2.next
                if l2 != None:
                    new_l.next = ListNode(0)
                    new_l = new_l.next
                # print listNodeToString(head)
        return head
