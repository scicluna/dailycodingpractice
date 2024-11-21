# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# initialize a hashmap
# if annagram... hashmap[annagram].append(string)
from collections import defaultdict

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    strmap = defaultdict(list)
    for string in strs:
        sorted_string = ''.join(sorted(string))
        strmap[sorted_string].append(string)
    return list(strmap.values())


