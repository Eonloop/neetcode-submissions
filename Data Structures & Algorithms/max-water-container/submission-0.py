class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxWaterAmount = 0

        while i < j:
            waterAmount = (j - i) * min(heights[i], heights[j])
            maxWaterAmount = max(maxWaterAmount, waterAmount)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxWaterAmount
        

        