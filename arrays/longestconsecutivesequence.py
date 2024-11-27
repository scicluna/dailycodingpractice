# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
# You must write an algorithm that runs in O(n) time.

# I need to loop over the numbers... Can't sort them...
# So without sorting... what do i do?

# 

def longestConsecutive(self, nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num-1 not in num_set:
            length = 1
            current = num

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)
            
    return longest