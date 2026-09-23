class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        pair = []

        for i in range(len(position)):
            pair.append((position[i], speed[i]))
        
        pair.sort(reverse=True)
        # print(pair)

        for p, s in pair:
            arr.append((target - p)/s)
            if len(arr) >= 2 and arr[-1] <= arr[-2]:
                arr.pop()

        return len(arr)