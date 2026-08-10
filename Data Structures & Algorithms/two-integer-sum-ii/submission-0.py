class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sortedNumbers = sorted(numbers)
        frontPointer = 0
        endPointer = len(numbers) - 1
        for i in range(len(numbers)):
            testVal = sortedNumbers[frontPointer] + sortedNumbers[endPointer]
            if (testVal == target):
                return [frontPointer + 1, endPointer + 1]
            if (testVal > target):
                endPointer -= 1
            else:
                frontPointer += 1
            

        