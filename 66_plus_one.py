class solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digit = "".join(str(digit) for digit in digits)
        numm = int(digit) + 1
        return [int(digit) for digit in str(numm)]
