class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0  # указатель на позицию следующего валидного элемента

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i  # k - количество элементов не равных val
