class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u_num = set(nums)
        if len(u_num) == len(nums):
            return False
        else:
            return True