# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# Make a hashmap from the list --- loop through hashmap for highest?
# def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#     numdict = {}
#     for num in nums:  
#         if num in numdict:
#             numdict[num] += 1
#         else:
#             numdict[num] = 1
#     return list(sorted(numdict, key=numdict.get))[-k:]

from collections import Counter
import heapq

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    # Count frequencies using Counter
    numdict = Counter(nums)
    # Use a heap to extract the k most frequent elements
    return [item for item, _ in heapq.nlargest(k, numdict.items(), key=lambda x: x[1])]
