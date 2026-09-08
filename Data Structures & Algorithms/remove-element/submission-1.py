class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_val_sum = 0
        for n in nums:
            if n != val:
                nums[not_val_sum] = n
                not_val_sum += 1
        return not_val_sum
