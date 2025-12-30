class Solution:
    def reversebeats(self, n:int) -> int:
        result = 0
        # Выносим константу из цикла
        for _ in range(32):
            result = (result << 1) + (n & 1)  # `+` иногда быстрее `|`
            n >>= 1
        return result
