# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Iterate over nums and place them into a map -> if already in a map return true, otherwise return false
def hasDuplicate(self, nums: list[int]) -> bool:
    nummap = {}
    for num in nums:
        if num in nummap:
            return True
        nummap[num] = 1
    return False


