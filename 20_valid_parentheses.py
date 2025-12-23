class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False
                if stack.pop() != pairs[char]:
                    return False
        return len(stack) == 0
