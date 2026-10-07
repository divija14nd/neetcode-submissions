class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if n-1 not in numSet:
                count = 1
                current = n

                while current+1 in numSet:
                    count+=1
                    current+=1
                
                res = max(count, res)
        return res