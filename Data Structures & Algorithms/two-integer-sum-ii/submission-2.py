class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []

        left, right = 0, len(numbers) - 1


        while left < right:
            addLR = numbers[left] + numbers[right]
            if addLR == target:
                result.append(left + 1)
                result.append(right + 1)
                return result
            elif addLR > target:
                right -= 1
            elif addLR < target:
                left += 1
        