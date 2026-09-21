class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = []
        res = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while arr and temp > temperatures[arr[-1]]:
                    # print(i, temp, arr[-1], temperatures[arr[-1]])
                    res[arr[-1]] = i - arr[-1]
                    arr.pop()
            arr.append(i)
        return res