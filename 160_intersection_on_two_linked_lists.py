class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
            
        # Два указателя, стартующие с голов списков
        pointerA = headA
        pointerB = headB
        
        # Двигаем указатели по спискам
        # Когда один достигает конца — перенаправляем его в голову другого списка
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
            
        # В точке пересечения (или None) указатели встретятся
        return pointerA
