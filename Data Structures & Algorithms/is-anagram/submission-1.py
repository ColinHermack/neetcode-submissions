class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurences = {}
        for letter in s:
            if letter not in occurences.keys():
                occurences[letter] = 1
            else:
                occurences[letter] += 1
        
        for letter in t:
            if letter not in occurences.keys():
                return False
            occurences[letter] -= 1

        for letter in s:
            if occurences[letter] != 0:
                return False

        return True
            