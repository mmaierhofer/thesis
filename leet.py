
from typing import List
from numpy import sort


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def twoSum(list1, list2):
    """
       :type x: int
       :rtype: bool
       """

    if not list1 and not list2:
        return list1
    if not list1 or not list2:
        return list1 if not list2 else list2
    seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
    head = seek
    while seek and target:
        while seek.next and seek.next.val < target.val:
            seek = seek.next
        seek.next, target = target, seek.next
        seek = seek.next
    return head


list1 = list({1, 2, 3})

print(twoSum({1, 2, 3}, {1, 2, 3}))
