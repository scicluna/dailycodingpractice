# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first. 

# place each number in list in a hashmap with their index as the pair
# loop over the list again. If the index isnt the same, and it equals target, add to it, and return
def twoSum(self, nums: list[int], target: int) -> list[int]:
    nummap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nummap:
            return [nummap[complement], i]
        nummap[num] = i