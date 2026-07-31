class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        letterDictS = defaultdict(int)
        for letter in s:
            letterDictS[letter] += 1
        letterDictT = defaultdict(int)
        for letter in t:
            letterDictT[letter] += 1

        if letterDictT == letterDictS:
            return True
        else:
            return False
