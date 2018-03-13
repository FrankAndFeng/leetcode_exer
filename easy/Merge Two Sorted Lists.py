# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll = ListNode(0)
        lc = ll

        while l1 or l2:
            if l1 == None:
                lc.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                lc.next = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    lc.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    lc.next = ListNode(l1.val)
                    l1 = l1.next
            lc = lc.next

        return ll.next
    
if __name__ == '__main__':



