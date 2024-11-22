# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

def encode(self, strs: list[str]) -> str:
    # use a generator for max efficiency - Basically its making a list at runtime with (f'{len(s)}:{s}' for s in strs) and since generators are iterables, it still works. Kind of confusing
    return ''.join(f'{len(s)}:{s}' for s in strs)

def decode(self, s: str) -> list[str]:
    decoded = []
    i = 0
    while i < len(s):
        # find the first instance of : marking a new string (since we split on number:)
        j = s.find(':', i)
        # find the length of the first string --- SINCE WE USED THE LENGTH AS THE SEPERATOR WOW
        length = int(s[i:j])
        # append the string from j+1 (after colon) to j+1+length (the length of the string)
        decoded.append(s[j + 1:j + 1 + length])
        # create new start
        i = j + 1 + length
    return decoded