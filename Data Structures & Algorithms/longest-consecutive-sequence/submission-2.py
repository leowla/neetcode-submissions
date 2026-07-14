class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # dedupe array using set
        nums = sorted(set(nums))

        consecutive_lengths = set()
        # consecutive run length = starting value (1) + number of comparisons
        consecutive_run = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                # count successful consecutive comparisons
                consecutive_run += 1
            else:
                # finished
                consecutive_lengths.add(consecutive_run)
                # reset
                consecutive_run = 1

        consecutive_lengths.add(consecutive_run)
        
        return max(consecutive_lengths)