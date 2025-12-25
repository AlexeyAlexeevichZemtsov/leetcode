
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Очищаем строку: только буквы и цифры, в нижнем регистре
        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
        # Сравниваем с обратной версией
        return cleaned == cleaned[::-1]
