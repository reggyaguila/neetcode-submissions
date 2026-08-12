class Solution:
    def search(self, nums: List[int], target: int, low=0, high=None) -> int:
        if high == None:
            high = len(nums) - 1
        if low > high:
            return -1
        
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        #What if Mid is < target?
        #Where does low need to start at
        if nums[mid] < target:
            return self.search(nums, target, mid+1, high)
        
        if nums[mid] > target:
            return self.search(nums, target, low, mid-1)


        