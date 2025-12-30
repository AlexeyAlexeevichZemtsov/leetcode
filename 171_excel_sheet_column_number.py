class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
    
# Обрабатываем строку слева направо.
    # На каждом шаге:
    # Умножаем текущий результат на 26 (сдвиг разрядов).
    # Добавляем значение текущей буквы (A=1, B=2, …, Z=26).

# Пример для "AB":
    # result = 0 * 26 + 1 = 1 (A)
    # result = 1 * 26 + 2 = 28 (B) → верно.

# Сложность: O(n) времени, O(1) памяти.
