class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        initial = Counter(s1)
        l = 0

        for i in range(len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1
        
            while i - l + 1> len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            # print(window)
            # print(initial)
            
            if window == initial:
                return True
        
        return False