# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        llen1 = l1
        llen2 = l2

        while llen1 is not None and llen2 is not None:
            llen1 = llen1.next
            llen2 = llen2.next

        if llen1 is None:
            h = llen = l2
        else:
            h = llen = l1
        sum_t = 0
        while l1 is not None and l2 is not None:
            llen.val = l1.val + l2.val + sum_t
            if llen.val >= 10:
                llen.val = llen.val - 10
                sum_t = 1
            else:
                sum_t = 0
            l1 = l1.next
            l2 = l2.next
            if sum_t == 1 and llen.next is None:
                llen.next = ListNode(0)
            llen = llen.next

        while llen is not None:
            llen.val = llen.val + sum_t
            if llen.val >= 10:
                llen.val = llen.val - 10
                sum_t = 1
                if llen.next is None:
                    llen.next = ListNode(0)
                
                llen = llen.next
            else:
                break

        return h
