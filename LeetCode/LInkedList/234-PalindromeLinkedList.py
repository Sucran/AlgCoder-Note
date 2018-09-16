# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val = []
        p_head = head
        if not head:
            return True
        if not head.next:
            return True
        while head:
            if val != []:
                last_val = val[-1]
                if last_val == head.val:
                    break
                if head.next:
                    if last_val == head.next.val:
                        break
            val.append(head.val)
            head = head.next
        if head == None:
            return False
        else:
            if head.next:
                if last_val == head.next.val:
                    head = head.next
            while head and val != []:
                if head.val != val.pop():
                    break
                head = head.next
            if head == None and val == []:
                return True
            else:
                return False