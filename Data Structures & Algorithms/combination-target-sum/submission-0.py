class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if start >= len(nums) or total > target:
                return
            
            curr.append(nums[start])
            dfs(start, curr, total+nums[start])
            curr.pop()
            dfs(start+1, curr, total)

        dfs(0, [], 0)

        return res