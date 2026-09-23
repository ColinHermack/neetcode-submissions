# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            head = list2
            list2 = list2.next
        elif list2 == None:
            head = list1
            list1 = list1.next
        elif list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        tail = head
        while list1 != None or list2 != None:
            if list1 == None:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
                continue
            if list2 == None:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
                continue
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        return head
        