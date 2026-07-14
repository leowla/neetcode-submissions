class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dedupe because dupes don't count in this scenario
        nums = set(nums)
        longest = 0
        
        for num in nums:
            # get the start of a consecutive sequence
            if num - 1 not in nums:
                current = num
                current_run = 1

                while current + 1 in nums:
                    current += 1
                    current_run += 1
            
                longest = max(longest, current_run)
        
        return longest