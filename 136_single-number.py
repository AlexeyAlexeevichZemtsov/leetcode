class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR накапливает уникальный элемент
        return result

# a ^ a = 0 — одинаковые числа обнуляются.
# a ^ 0 = a — уникальное число остаётся.
# Порядок операций не важен (XOR коммутативен).

# Пример:
# nums = [4, 1, 2, 1, 2]
# 0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 (все пары обнулились).
