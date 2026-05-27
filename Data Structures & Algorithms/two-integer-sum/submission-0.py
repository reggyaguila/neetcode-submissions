class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Okay, here's what we do.
        #We can insert our entire list into a dictionary
        #And then subtract the target from current value, which will return a value
            #We can then use that value to search for where that value exists in our dict
            #But we can't use the values as keys because we could have duplicate values
            #But if we use indicies as keys, how do we search for a key
        #If we have a dictionary, what should be the key and what should be the value
        two_sum_dict = {}
        for i,n in enumerate(nums):
            if (target - n) in two_sum_dict:
                t = (i, two_sum_dict[target-n])
                return sorted(list(t))
            else:
                two_sum_dict[n] = i

        