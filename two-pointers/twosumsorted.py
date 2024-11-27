# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. 
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
# There will always be exactly one valid solution.
# Your solution must use O(1) additional space.

def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers)-1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left+1, right+1]
        if current_sum < target:
            left += 1
        if current_sum > target:
            right -= 1
    return [0, 0]
