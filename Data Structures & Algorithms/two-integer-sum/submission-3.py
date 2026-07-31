class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lockedIndex = 0
        for lockedIndex in range (0, len(nums)):
            for i in range(1, len(nums)):
                if i == lockedIndex:
                    continue 
                newNum = nums[lockedIndex] + nums[i]
                if newNum == target:
                    return [lockedIndex, i]
                else:
                    continue;
 
            

            