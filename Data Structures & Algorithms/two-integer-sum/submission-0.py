class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resDic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in resDic:
                return [resDic[diff], i]
            resDic[nums[i]] = i