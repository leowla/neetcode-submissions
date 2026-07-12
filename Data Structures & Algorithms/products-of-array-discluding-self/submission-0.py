class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # multiply all numbers before i
        prefix = 1
        for i in range(n):
            output[i] *= prefix
            prefix *= nums[i]

        # multiply all numbers after i
        suffix = 1
        for i in reversed(range(n)):
            output[i] *= suffix
            suffix *= nums[i]

        return output