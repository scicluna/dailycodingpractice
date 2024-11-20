# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
def isAnagram(self, s: str, t: str) -> bool:
    stringmap = {}
    for letter in s:
        if letter not in stringmap:
            stringmap[letter] = 1
        else:
            stringmap[letter] += 1
    for letter2 in t:
        if letter2 not in stringmap:
            return False
        else:
            stringmap[letter2] -= 1
            if stringmap[letter2] < 0:
                return False
    return True

            