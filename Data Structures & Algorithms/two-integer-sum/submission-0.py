class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in h:
                return [h[temp], i]
            h[nums[i]] = i
        