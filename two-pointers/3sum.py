# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

def threeSum(self, nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, number in enumerate(nums): # loop each iteration, then do two point
        if number > 0:
            break # because if its greater than 0, then our sorted list cannot go any further

        if i > 0 and number == nums[i-1]:
            continue #if i isn't the first element, and we run into a duplicate number, skip an itertation

        left = i+1
        right = len(nums)-1

        while left < right:
            three_sum = number + nums[left] + nums[right] # look to see what the current iteration + two pointers is...
            if three_sum > 0: # if its > 0, move the greater poitner (right) to the left one
                right -= 1
            elif three_sum < 0:
                left += 1 # if its < 0, move the left pointer to the right (since left is smallest)
            else:
                res.append([number, nums[left], nums[right]]) # append if it equals 0
                left += 1 #move left and right
                right -= 1 
                while nums[left] == nums[left-1] and left < right: 
                    left += 1 #move over duplicates if possible
    return res