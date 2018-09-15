# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        p_faster = head.next
        p_slower = head
        while p_faster and p_slower:
            p_faster = p_faster.next
            p_slower = p_slower.next
            if p_faster:
                p_faster = p_faster.next
            if p_faster is p_slower:
                return True
        return False