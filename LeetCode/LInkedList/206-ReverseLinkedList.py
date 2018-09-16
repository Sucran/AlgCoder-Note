# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_list = []
        if head == None:
            return None
        while head:
            node_list.append(head)
            head = head.next

        for i in range(len(node_list) - 1, -1, -1):
            if i == 0:
                node_list[i].next = None
            else:
                node_list[i].next = node_list[i - 1]
        start = len(node_list) - 1
        return node_list[start]
