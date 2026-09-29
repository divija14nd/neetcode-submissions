class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        prod = 1 
        for n in nums:
            if n != 0:
                prod *= n

        res = []
        for n in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                res.append(prod if n == 0 else 0)
            else:
                res.append(prod // n)

        return res
