class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            i = nums[n]
            j = target - i
            if j in nums:
                m = nums.index(j)
                if n != m:
                    return sorted([n, m])
        return False