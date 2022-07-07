# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None):
            return list2
        if list2 == None:
            return list1
        resList = ListNode()
        head = resList
        prev = None
        while list1!=None and list2!=None:
            if(list1.val<list2.val):
                resList.val = list1.val
                list1 = list1.next
            else:
                resList.val = list2.val
                list2 = list2.next
            if(prev!=None):
                prev.next = resList
            prev = resList
            resList = ListNode()
        while list1:
            resList.val = list1.val
            prev.next = resList
            prev = resList
            resList = ListNode()
            list1 = list1.next
        while list2:
            print("here",list2.val)
            resList.val = list2.val
            prev.next = resList
            prev = resList
            resList = ListNode()
            list2 = list2.next
        return head
        