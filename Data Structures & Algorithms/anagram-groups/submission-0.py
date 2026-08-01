class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringDict = defaultdict(list)
        returnArray = []
        for string in strs:
            sortedString = "".join(sorted(string))
            stringDict[sortedString].append(string)
        for key in stringDict:
            returnArray.append(stringDict[key])
        return returnArray
                
            
            