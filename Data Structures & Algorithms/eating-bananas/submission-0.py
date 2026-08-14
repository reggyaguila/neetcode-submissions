import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int, best=None, low=1, high=None) -> int:
        if high == None:
            high = max(piles)
        if best == None:
            best = high

        if low > high:
            return best

        mid = (low + high) // 2

        total_hours = 0
        for i in piles:
            total_hours += math.ceil(i / mid)

        if total_hours > h:
            return self.minEatingSpeed(piles, h, best, mid + 1, high)
        if total_hours <= h:
            best = mid
            return self.minEatingSpeed(piles, h, best, low, mid - 1)