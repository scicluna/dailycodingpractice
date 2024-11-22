# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    # calculate prefixes
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    # this gets us an array where every result is the product of all numbers before it?


    # calculate suffixces
    suffix = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    # this multiplies the indexes in the array in reverse order starting from the point, so gets product of all numbers after it? wtf

    return result