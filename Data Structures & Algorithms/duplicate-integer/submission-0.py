class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testArray = []
        for num in nums:
            if num not in testArray:
                testArray.append(num)
            else: 
                return True
        return False
            
            
        