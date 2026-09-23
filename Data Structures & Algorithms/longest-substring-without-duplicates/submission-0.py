class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        window = set()
        start = 0
        best = 0

        window.add(s[start])

        for end in range(1, len(s), 1):
            while (s[end] in window):
                window.remove(s[start])
                start += 1
            window.add(s[end])
            best = max(best, len(window))
        
        return best