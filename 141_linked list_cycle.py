# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
            
        slow = fast = head
        
        while fast.next and fast.next.next:  # Проверяем возможность двух шагов сразу
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # 'is' вместо '==' для проверки идентичности объектов
                return True
        return False
