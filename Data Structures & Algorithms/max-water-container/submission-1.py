class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        start, end = 0, len(heights) - 1
        
        result = 0

        while (start < end):
            width = end - start

            shorter_height = min(heights[start], heights[end])

            local_result = width * shorter_height

            result = max(local_result, result)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return result