class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    return
                curr.append(nums[i])
                dfs(i, curr, total+nums[i])
                curr.pop()

        dfs(0, [], 0)

        return res